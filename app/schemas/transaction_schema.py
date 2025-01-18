from pydantic import BaseModel

class TransactionCreate(BaseModel):
    mf_name: str
    quantity: int
