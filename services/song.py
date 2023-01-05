from schemas.song import Song
from models.song import Song as SongModel

class SongService():

    def __init__(self, db) -> None:
        self.db = db
    

    def get_songs(self):
        response = self.db.query(SongModel).all()
        return response


    def get_song(self, id: int):
        response = self.db.query(SongModel).filter(SongModel.id == id).first()
        return response


    def get_song_by_artist(self, artist: str):
        response = self.db.query(SongModel).filter(SongModel.song_artist == artist)
        return response


    def add_song(self, data: Song):
        new_song = SongModel(**data.dict())
        self.db.add(new_song)
        self.db.commit()
        return


    def update_song(self, id: int, data: Song):
        song = self.db.query(SongModel).filter(SongModel.id == id).first()
        song.cover_page = data.cover_page
        song.song_name = data.song_name
        song.song_artist = data.song_artist
        song.song_length = data.song_length
        song.like = data.like
        self.db.commit()
        return


    def delete_song(self, id: int):
        song = self.db.query(SongModel).filter(SongModel.id == id).first()
        self.db.delete(song)
        self.db.commit()
        return