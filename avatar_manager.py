from typing import Optional

from avatar_searcher_service import IAvatarSearchService
from avatar_storage_service import IAvatarStorage
from avatar_exceptions import AvatarUploadError, AvatarNotFoundError
from logger import logger


class AvatarManager:
    def __init__(self, avatar_storage: IAvatarStorage, avatar_searcher: IAvatarSearchService) -> None:
        self.avatar_searcher = avatar_searcher
        self.avatar_storage = avatar_storage

    def find_and_store_user_avatar(self, user_email: str) -> Optional[str]:
        try:
            avatar_url = self.avatar_searcher.find_avatar_by_email(user_email)
            if avatar_url is None:
                raise AvatarNotFoundError(f"Avatar not found for the given email: {user_email}")

            s3_file_path = self.avatar_storage.upload_avatar(avatar_url)
            if not s3_file_path:
                raise AvatarUploadError("Failed to upload avatar to S3.")

            return s3_file_path

        except AvatarNotFoundError as e:
            logger.error(e)
        except AvatarUploadError as e:
            logger.error(e)
        except Exception as e:
            logger.exception(f"Unexpected error occurred: {e}")

    def generate_temporary_link(self, file_path: str):
        return self.avatar_storage.generate_temporary_link(file_path)
