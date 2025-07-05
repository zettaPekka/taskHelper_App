from typing import Literal

from pydantic import BaseModel
from fastapi import UploadFile


class TextTask(BaseModel):
    text: str
    action: str


class PhotoTask(BaseModel):
    photo: UploadFile
    action: Literal["help", "answer"]