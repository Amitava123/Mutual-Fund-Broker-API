from pydantic import BaseModel
from typing import List

# Define the Fund schema (the details of a mutual fund)
class FundBase(BaseModel):
    name: str
    nav: float  # Net Asset Value

# Response model for returning Fund data
class FundOut(FundBase):
    id: int

    class Config:
        orm_mode = True

# For representing the fund within a user's portfolio
class PortfolioFundOut(BaseModel):
    fund_id: int
    quantity: int

    class Config:
        orm_mode = True

# For adding funds to the system
class FundCreate(FundBase):
    pass

# Portfolio schema for user's funds and total investments
class PortfolioOut(BaseModel):
    funds: List[PortfolioFundOut]
    initial_investment: float
    profit_loss: float = 0.0  # This will be calculated dynamically based on the portfolio's value

    class Config:
        orm_mode = True
