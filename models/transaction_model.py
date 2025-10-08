from sqlalchemy import Column, ForeignKey, Integer, String, Float
from config.settings import Base, db_engine

class TransactionModel(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    date = Column(String)

# Base.metadata.create_all(bind=db_engine)