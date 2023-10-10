from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.services import service_cliente as service
from app.utils.viacep import validate_address
from app.models.model_cliente import ClienteDB, ClienteSchema
from app.database.db import SessionLocal


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/", response_model=ClienteDB, status_code=201)
def create_cliente(*, db: Session = Depends(get_db), payload: ClienteSchema):
        # Validação do endereço usando a API ViaCEP
    if not validate_address(payload.cep):
        raise HTTPException(status_code=400, detail="Endereço inválido")

    cliente = service.post(db_session=db, payload=payload)
    return cliente


@router.get("/{id}/", response_model=ClienteDB)
def read_cliente(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0),
):
    cliente = service.get(db_session=db, id=id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return cliente


@router.get("/", response_model=List[ClienteDB])
def read_all_clientes(db: Session = Depends(get_db)):
    return service.get_all(db_session=db)


@router.put("/{id}/", response_model=ClienteDB)
def update_cliente(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0), payload: ClienteSchema
):
    cliente = service.get(db_session=db, id=id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    
        # Validação do endereço usando a API ViaCEP
    if not validate_address(payload.cep):
        raise HTTPException(status_code=400, detail="Endereço inválido")

    cliente = service.put(
        db_session=db, cliente=cliente, nome=payload.nome, cpf=payload.cpf, cep=payload.cep, endereco=payload.endereco, telefone=payload.telefone
    )
    return cliente
