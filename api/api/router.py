from http import HTTPStatus
from typing import Final, Sequence

from fastapi import APIRouter, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .repository import Repository
from .models import User

USERS: Final[Repository[User]] = Repository()

router: APIRouter = APIRouter()


def assert_user_exists(id: int, /) -> None:
    if not USERS.has(id):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)


@router.post("/")
def users_create(name: str, occupation: str) -> JSONResponse:
    user: User = User(id=USERS.index, name=name, occupation=occupation)

    USERS.add(user)

    return JSONResponse(
        status_code=HTTPStatus.CREATED,
        content=jsonable_encoder(user),
    )


@router.get("/")
def users_list() -> Sequence[User]:
    return USERS.list()


@router.get("/{id}")
def users_get(id: int) -> User:
    assert_user_exists(id)

    return USERS.get(id)


@router.put("/")
def users_update(user: User) -> Response:
    assert_user_exists(user.id)

    USERS.delete(user.id)
    USERS.add(user)

    return Response(status_code=HTTPStatus.NO_CONTENT)


@router.delete("/{id}")
def users_delete(id: int) -> Response:
    assert_user_exists(id)

    USERS.delete(id)

    return Response(status_code=HTTPStatus.NO_CONTENT)
