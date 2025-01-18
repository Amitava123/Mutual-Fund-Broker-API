from pydantic import BaseModel

class PortfolioOut(BaseModel):
    id: int
    total_value: float
    class Config:
        orm_mode = True
