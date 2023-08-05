from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
