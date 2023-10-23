from abc import ABC, abstractmethod
from typing import Optional


class IAvatarStorage(ABC):
    @abstractmethod
    def upload_avatar(self, avatar_url: str) -> Optional[str]:
        pass

    @abstractmethod
    def generate_temporary_link(self, file_path: str) -> Optional[str]:
        pass
