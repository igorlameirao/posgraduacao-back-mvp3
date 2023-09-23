from pydantic import BaseModel

class UsuarioReqModel(BaseModel):
    id: int
    nome: str
    sobrenome: str
    cep: str
    logradouro: str
    complemento: str
    bairro: str