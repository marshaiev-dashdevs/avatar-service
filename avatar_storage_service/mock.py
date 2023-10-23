from .interface import IAvatarStorage
from typing import Optional


class MockAvatarStorage(IAvatarStorage):
    SUCCESS = True
    MOCKED_URL = "avatars/mock.jpg"

    def upload_avatar(self, avatar_url: str) -> Optional[str]:
        if self.SUCCESS:
            return self.MOCKED_URL

    def generate_temporary_link(self, file_path: str) -> Optional[str]:
        if self.SUCCESS:
            return self.MOCKED_URL
