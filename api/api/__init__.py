from http import HTTPStatus
from typing import Final, Mapping

from fastapi import FastAPI, HTTPException

from .models import User

app: FastAPI = FastAPI()

USERS: Final[Mapping[int, User]] = {
    1: User(id=1, name="Sam", occupation="Dentist"),
}


@app.get("/user/{id}")
def foo(id: int) -> User:
    if id not in USERS:
        raise HTTPException(HTTPStatus.NOT_FOUND)

    return USERS[id]
