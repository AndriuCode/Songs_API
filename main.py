from fastapi import FastAPI
from config.database import Base, engine


app = FastAPI()
app.title = "Your Songs - API"

Base.metadata.create_all(bind=engine)