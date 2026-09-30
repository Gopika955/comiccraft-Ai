from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from app import routes
import os

load_dotenv()
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
app.include_router(routes.router)

