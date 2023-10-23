import uuid
import requests

from boto3_helpers import handle_s3_exceptions
from logger import logger
from .interface import IAvatarStorage
from typing import Optional


class S3AvatarStorage(IAvatarStorage):
    def __init__(self, bucket_name, s3_client):
        self.bucket_name = bucket_name
        self.s3_client = s3_client

    @handle_s3_exceptions
    def upload_avatar(self, avatar_url: str) -> Optional[str]:
        response = requests.get(avatar_url)
        if response.status_code == 200:
            file_name = str(uuid.uuid4()) + '.jpg'
            s3_file_path = f'avatars/{file_name}'
            self.s3_client.put_object(Body=response.content, Bucket=self.bucket_name, Key=s3_file_path)
            return s3_file_path
        else:
            logger.error(f"Failed to fetch avatar from URL: {avatar_url}, Status Code: {response.status_code}")

    @handle_s3_exceptions
    def generate_temporary_link(self, s3_file_path: str) -> Optional[str]:
        if not isinstance(s3_file_path, str):
            logger.error("Invalid type for s3_file_path. Expected str.")
            return None

        try:
            response = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': s3_file_path},
                ExpiresIn=3600
            )
            return response
        except Exception as e:
            logger.exception(f"Failed to generate temporary link for {s3_file_path}: {e}")
            return None
