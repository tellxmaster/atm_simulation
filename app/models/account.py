# models/account.py

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String(255), unique=True, index=True)  # Especifica la longitud aquí
    owner_name = Column(String(255))  # Aquí también, si es necesario
    balance = Column(Float)


    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
