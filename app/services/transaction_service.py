from app.services.rapidapi_service import get_nav
from app.models.transaction_model import Transaction
from app.models.portfolio_model import Portfolio
from sqlalchemy.orm import Session
from fastapi import HTTPException

class TransactionService:
    @staticmethod
    def buy_mutual_fund(db: Session, portfolio: Portfolio, mf_name: str, quantity: int):
        nav = get_nav(mf_name)
        if not nav:
            raise HTTPException(status_code=400, detail="Failed to fetch NAV from API")
        
        total_price = nav * quantity
        portfolio.total_value += total_price

        db_transaction = Transaction(
            portfolio_id=portfolio.id,
            mf_name=mf_name,
            quantity=quantity,
            price_per_unit=nav
        )

        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)

        return {"message": "Mutual Fund Purchased", "transaction_id": db_transaction.id, "amount": total_price}

    @staticmethod
    def sell_mutual_fund(db: Session, portfolio: Portfolio, mf_name: str, quantity: int):
        nav = get_nav(mf_name)
        if not nav:
            raise HTTPException(status_code=400, detail="Failed to fetch NAV from API")
        
        total_value = nav * quantity
        portfolio.total_value -= total_value

        db_transaction = Transaction(
            portfolio_id=portfolio.id,
            mf_name=mf_name,
            quantity=-quantity,
            price_per_unit=nav
        )

        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)

        return {"message": "Mutual Fund Sold", "transaction_id": db_transaction.id, "amount": total_value}
