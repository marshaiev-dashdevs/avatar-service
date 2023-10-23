from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from logger import logger
from .interface import IAvatarSearchService
from typing import Optional


class SlackAvatarSearcher(IAvatarSearchService):
    def __init__(self, token: str) -> None:
        self.client = WebClient(token=token)

    def find_avatar_by_email(self, email: str) -> Optional[str]:
        try:
            response = self.client.users_lookupByEmail(email=email)
            user = response["user"]
            if "image_512" in user:
                avatar_url = user["image_512"]
                return avatar_url
            else:
                return None
        except SlackApiError as e:
            logger.error(f"Error fetching avatar for {email}: {e.response['error']}")
            return None
