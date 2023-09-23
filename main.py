from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from entities import Usuario, Session
# from dtos.request import UsuarioReqModel

from controllers.usuario_controller import include_route as usuario_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


usuario_controller(app)