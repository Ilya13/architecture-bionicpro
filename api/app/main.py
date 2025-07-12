
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.api.endpoints import router
from app.api.handlers import exception_handler
from app.dependencies import keycloak_auth


app = FastAPI(
    title='BionicPRO Reports FastAPI',
    description='API для передачи отчётов',
    docs_url='/swagger-ui',
    openapi_url='/openapi.json',
    version=__version__,
    dependencies=[Depends(keycloak_auth)],
)

app.include_router(router)
app.add_exception_handler(Exception, exception_handler)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
