from fastapi import Depends, FastAPI

from .dependencies import auth
from .router import router

app: FastAPI = FastAPI(
    # dependencies=[Depends(auth)],
)

app.include_router(router, prefix="/users")
