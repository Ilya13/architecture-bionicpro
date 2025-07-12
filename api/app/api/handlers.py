from fastapi.responses import JSONResponse

import requests
from app.api.exceptions import APIException
from app.api.models.responses import BaseResponse


def exception_handler(request: requests.Request, exc: Exception):
    if isinstance(exc, APIException):
        status_code = exc.status_code
        message = exc.message or str(exc)
    else:
        status_code = 500
        message = 'Internal Server Error'
    content = BaseResponse(message=message).dict()

    return JSONResponse(
        status_code=status_code,
        content=content,
    )
