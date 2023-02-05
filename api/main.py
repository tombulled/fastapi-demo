from fastapi import Depends, FastAPI, Request, Response

from .dependencies import auth
from .router import router

app: FastAPI = FastAPI(
    # dependencies=[Depends(auth)],
)


@app.middleware("http")
def log_request(request: Request, call_next) -> Response:
    print("Logging Request:", request.__dict__)

    return call_next(request)


app.include_router(router, prefix="/users")
