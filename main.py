import configparser

import uvicorn
from fastapi import FastAPI

from config import settings

HOST = settings["SERVER"]["LOCAL_HOST"]
PORT = settings["SERVER"]["SERVICE_PORT"]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
