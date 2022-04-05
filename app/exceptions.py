from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.auth import NotAuthorized
from app.core.exceptions import NotFound


def register_exceptions(app: FastAPI) -> None:
    """Function to set handle exceptions from core functions"""

    @app.exception_handler(NotAuthorized)
    async def not_authorized_handler(request: Request, exception: NotAuthorized):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"msg": "Not authorized"}
        )

    @app.exception_handler(NotFound)
    async def not_found_handler(request: Request, exception: NotFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"msg": str(exception)}
        )
