# app/controllers/account_controller.py

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from ..models.account import Account
from ..schemas.account_schema import AccountCreate, Account as AccountSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/accounts/", response_model=AccountSchema)
def create_account(account_data: AccountCreate, db: Session = Depends(get_db)):
    new_account = Account(account_number=account_data.account_number, owner_name=account_data.owner_name)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

@router.get("/accounts/{account_id}", response_model=AccountSchema)
def get_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if account:
        return account
    raise HTTPException(status_code=404, detail="Cuenta no encontrada")

@router.get("/accounts/{account_id}/balance", response_model=AccountSchema)
def get_balance(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return account

@router.get("/accounts/", response_model=List[AccountSchema])
def get_accounts(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return accounts
