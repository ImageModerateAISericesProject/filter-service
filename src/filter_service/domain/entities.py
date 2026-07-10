from dataclasses import dataclass
from enum import Enum


class StatusType(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class Post:
    """НА БУДУЩЕЕ))"""

    post_id: int
    images_list: list[Image]


@dataclass
class Image:
    id: int
    link: str  # линк на S3
    source: str
    status: StatusType
    post_id: int
