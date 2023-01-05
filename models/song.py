from config.database import Base
from sqlalchemy import Boolean, Column, Float, Integer, String 

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    cover_page = Column(String)
    song_name = Column(String)
    song_artist = Column(String)
    song_length = Column(Float)
    like = Column(Boolean)