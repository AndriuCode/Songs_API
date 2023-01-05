from typing import Optional
from pydantic import BaseModel, Field

class Song(BaseModel):
    id: Optional[int] = None
    cover_page: str
    song_name: str = Field(min_length=5, max_length=400)
    song_artist: str = Field(min_length=5)
    song_length: float = Field(ge=0.30)
    like: bool

    class Config:
        schema_extra = {
            "example": {
                'id': 1,
                'cover_page': "https://your_img_url.com",
                'song_name': "Nombre de la canción",
                'song_artist': "Nombre del autor de la canción",
                'song_length': 3.40,
                'like': True
            }
        }