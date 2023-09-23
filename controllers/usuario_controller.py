from fastapi import FastAPI, APIRouter

from dtos.request import UsuarioReqModel
from entities import Usuario, Session

router = APIRouter(prefix='/usuarios', tags=["Usuarios"])


@router.post("")
def criar_usuario(model: UsuarioReqModel):
    usuario = Usuario(nome=model.nome, sobrenome=model.sobrenome, cep=model.cep, logradouro=model.logradouro, complemento=model.complemento, bairro=model.bairro)
    session = Session()
    session.add(usuario)
    session.commit()
    usuarios = session.query(Usuario).all()
    return usuarios

@router.delete("")
def excluir_usuario(id: int):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.id == id).first()
    session.delete(usuario)
    session.commit()
    return {"success": True, "message": "Usuario criado com sucesso!"}

@router.get("")
def get_usuarios():
    session = Session()
    usuarios = session.query(Usuario).all()
    return usuarios


@router.get("/{id}")
def get_usuarios_by_id(id: int):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.id == id).first()
    return usuario


@router.put("")
def alterar(model: UsuarioReqModel):
    session = Session()
    session.query(Usuario).filter(Usuario.id == model.id)\
        .update({'nome': model.nome, 'sobrenome': model.sobrenome, 'cep': model.cep,  
                 'logradouro': model.logradouro,  'complemento': model.complemento,  'bairro': model.bairro})
    session.commit()
    usuarios = session.query(Usuario).all()
    return usuarios


def include_route(app: FastAPI):
    app.include_router(router)
