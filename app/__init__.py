from fastapi import FastAPI
from .routes import app as router

app = FastAPI()
app.include_router(router, prefix="/api")
