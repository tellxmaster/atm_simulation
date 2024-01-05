# app/controllers/transaction_controller.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from ..models.transaction import Transaction
from ..models.account import Account
from ..schemas.transaction_schema import TransactionCreate, Transaction as TransactionSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions/", response_model=TransactionSchema)
def create_transaction(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == transaction_data.account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    
    if transaction_data.transaction_type == 'deposit':
        account.deposit(transaction_data.amount)
    elif transaction_data.transaction_type == 'withdraw':
        if not account.withdraw(transaction_data.amount):
            raise HTTPException(status_code=400, detail="Fondos insuficientes")
    else:
        raise HTTPException(status_code=400, detail="Tipo de transacción no válido")

    new_transaction = Transaction(
        account_id=transaction_data.account_id,
        transaction_type=transaction_data.transaction_type,
        amount=transaction_data.amount
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction
