from .interface import IAvatarSearchService
from typing import Optional


class MockAvatarSearcher(IAvatarSearchService):
    SUCCESS = True
    MOCKED_URL = "https://example.com/avatars/mock.jpg"

    def find_avatar_by_email(self, email: str) -> Optional[str]:
        if self.SUCCESS:
            return self.MOCKED_URL
