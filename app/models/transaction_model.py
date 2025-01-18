from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))
    mf_name = Column(String)
    quantity = Column(Integer)
    price_per_unit = Column(Float)

    portfolio = relationship("Portfolio", back_populates="transactions")
