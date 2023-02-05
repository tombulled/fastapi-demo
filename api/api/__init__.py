from typing import Mapping

from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
def get_root() -> Mapping[str, str]:
    return {"message": "Hello, World!"}
