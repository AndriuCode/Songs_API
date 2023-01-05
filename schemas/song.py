from typing import Optional
from pydantic import BaseModel, Field

class Song(BaseModel):
    id: Optional(int) = None
    cover_page: str
    song_name: str
    song_artist: str
    song_length: float
    like: bool