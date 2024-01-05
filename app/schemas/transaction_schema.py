from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionCreate(BaseModel):
    account_id: int
    amount: float
    transaction_type: str

class Transaction(BaseModel):
    id: int
    account_id: int
    transaction_type: str
    amount: float
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True
