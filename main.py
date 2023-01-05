from fastapi import FastAPI
from routers.song import song_router
from config.database import Base, engine
from middlewares.error_handler import ErroHandler


app = FastAPI()
app.title = "Your Songs - API"

app.add_middleware(ErroHandler)

app.include_router(song_router)

Base.metadata.create_all(bind=engine)