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

class SourceType(str, Enum):
    REVIEWS = "reviews"
    GOODS = "goods"

@dataclass
class IncomingImage:
    """Получаем"""
    id:int
    link:str
    source:SourceType
    status:StatusType
    post_id:int

