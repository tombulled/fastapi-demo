from http import HTTPStatus

from fastapi import Header, HTTPException


def auth(x_token: str = Header()) -> None:
    if x_token != "waffles":
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Nice try, Jerry!"
        )
