from typing import List
from fastapi import APIRouter
from schemas.song import Song
from config.database import Session
from services.song import SongService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

song_router = APIRouter()

@song_router.get('/songs', tags=['Song - CRUD'], response_model=List[Song])
def get_songs() -> List[Song]:
    db = Session()
    response = SongService(db).get_songs()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@song_router.get('/songs/{id}', tags=['Song - CRUD'], response_model=Song)
def get_song(id) -> Song:
    db = Session()
    response = SongService(db).get_song(id)
    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado canción con ese ID"})
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@song_router.get('/song/', tags=['Song - CRUD'], response_model=List[Song])
def get_song_by_artist(artist) -> List[Song]:
    db = Session()
    response = SongService(db).get_song_by_artist(artist)
    if not response:
        return JSONResponse(status_code=404, content={"message": "No se han encontrado canciones pertenecientes a ese artista"})
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@song_router.post('/song', tags=['Song - CRUD'], response_model=dict)
def add_song(song: Song) -> dict:
    db = Session()
    SongService(db).add_song(song)
    return JSONResponse(status_code=201, content={"message": "Se a añadido exitosamente la canción a tu biblioteca"})


@song_router.put('/song/{id}', tags=['Song - CRUD'], response_model=dict)
def update_song(id: int, song: Song) -> dict:
    db = Session()
    song_confirmation =  SongService(db).get_song(id)
    if not song_confirmation:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado canción con ese ID"})
    SongService(db).update_song(id, song)
    return JSONResponse(status_code=200, content={"message": "Se ha actualizado exitosamente los datos de la canción"})


@song_router.delete('/song/{id}', tags=['Song - CRUD'], response_model=dict)
def delete_song(id: int) -> dict:
    db = Session()
    song_confirmation =  SongService(db).get_song(id)
    if not song_confirmation:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado canción con ese ID"})
    SongService(db).delete_song(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado exitosamente la canción de su biblioteca"})