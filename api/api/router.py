from http import HTTPStatus
from typing import Final, Sequence

from fastapi import APIRouter, HTTPException, Response

from .repository import Repository
from .models import User

USERS: Final[Repository[User]] = Repository()

router: APIRouter = APIRouter()


def assert_user_exists(id: int, /) -> None:
    if not USERS.has(id):
        raise HTTPException(HTTPStatus.NOT_FOUND)


@router.post("/")
def users_create(name: str, occupation: str) -> User:
    user: User = User(id=USERS.index, name=name, occupation=occupation)

    USERS.add(user)

    return user


@router.get("/")
def users_list() -> Sequence[User]:
    return USERS.list()


@router.get("/{id}")
def users_get(id: int) -> User:
    assert_user_exists(id)

    return USERS.get(id)


@router.delete("/{id}")
def users_delete(id: int) -> Response:
    assert_user_exists(id)

    USERS.delete(id)

    # If a DELETE method is successfully applied, the origin server SHOULD send
    #   * a 202 (Accepted) status code if the action will likely succeed but has
    #     not yet been enacted,
    #   * a 204 (No Content) status code if the action has been enacted and no
    #     further information is to be supplied, or
    #   * a 200 (OK) status code if the action has been enacted and the response
    #     message includes a representation describing the status.
    # (RFC 9110: HTTP Semantics, Section 9.3.5)
    return Response(status_code=HTTPStatus.NO_CONTENT)
