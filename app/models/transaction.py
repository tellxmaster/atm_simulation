# models/transaction.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    transaction_type = Column(String(255))
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    

    account = relationship("Account")

    def __init__(self, account_id, transaction_type, amount):
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
