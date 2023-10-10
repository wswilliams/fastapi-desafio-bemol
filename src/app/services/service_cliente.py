from sqlalchemy.orm import Session

from app.models.model_cliente import Cliente, ClienteSchema


def post(db_session: Session, payload: ClienteSchema):
    cliente = Cliente(nome=payload.nome, cpf=payload.cpf, cep=payload.cep, endereco=payload.endereco, telefone=payload.telefone)
    db_session.add(cliente)
    db_session.commit()
    db_session.refresh(cliente)
    return cliente


def get(db_session: Session, id: int):
    return db_session.query(Cliente).filter(Cliente.id == id).first()


def get_all(db_session: Session):
    return db_session.query(Cliente).all()


def put(db_session: Session, cliente: Cliente, nome: str, cpf: str, cep: str, endereco: str, telefone: str):
    cliente.nome = nome
    cliente.cpf = cpf
    cliente.cep = cep
    cliente.endereco = endereco
    cliente.telefone = telefone
    db_session.commit()
    return cliente
