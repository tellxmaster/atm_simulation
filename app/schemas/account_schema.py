from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_number: str
    owner_name: str

class Account(BaseModel):
    id: int
    account_number: str
    owner_name: str
    balance: float

    class Config:
        orm_mode = True
