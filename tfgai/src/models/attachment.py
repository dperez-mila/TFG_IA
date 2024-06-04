
from dataclasses import dataclass

from .model import Model
from ..enums import FileExtension


@dataclass
class Attachment(Model):
    submission_id: str
    file_name: str
    file_extension: FileExtension
    file_size: float
    file_url: str

