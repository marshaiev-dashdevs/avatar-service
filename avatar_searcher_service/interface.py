from abc import ABC, abstractmethod
from typing import Optional


class IAvatarSearchService(ABC):
    @abstractmethod
    def find_avatar_by_email(self, email: str) -> Optional[str]:
        pass
