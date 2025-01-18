from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

# class Fund(Base):
#     __tablename__ = "funds"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     nav = Column(Float)
    
#     portfolios = relationship("PortfolioFund", back_populates="fund")
    
#     def __repr__(self):
#         return f"<Fund(name={self.name}, nav={self.nav})>"

# class PortfolioFund(Base):
#     __tablename__ = "portfolio_funds"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id")) 
#     fund_id = Column(Integer, ForeignKey("funds.id"))
#     quantity = Column(Integer)
    
#     fund = relationship("Fund", back_populates="portfolios")
#     user = relationship("User", back_populates="portfolio")
    
#     def __repr__(self):
#         return f"<PortfolioFund(user_id={self.user_id}, fund_id={self.fund_id}, quantity={self.quantity})>"
