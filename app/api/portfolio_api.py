from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from app.database.session import get_db
from app.schemas.portfolio_schema import *
from app.models import user_model
from app.schemas import fund_schema
from app.models import fund_model

router = APIRouter()

@router.get("/portfolio/{user_id}", response_model=PortfolioOut)
def get_portfolio(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        return db_user.portfolio
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/dashboard/{user_id}", response_model=PortfolioOut)
def get_dashboard(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        portfolio = db_user.portfolio
        total_value = sum(fund.quantity * fund.nav for fund in portfolio.funds)
        profit_loss = total_value - portfolio.initial_investment
        portfolio.profit_loss = profit_loss
        return portfolio
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/buy/{user_id}", response_model=PortfolioOut)
def buy_fund(user_id: int, fund_id: int, quantity: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    db_fund = db.query(fund_model.Fund).filter(fund_model.Fund.id == fund_id).first()
    
    if db_user and db_fund:
        fund_in_portfolio = next((f for f in db_user.portfolio.funds if f.id == fund_id), None)
        if fund_in_portfolio:
            fund_in_portfolio.quantity += quantity
        else:
            db_user.portfolio.funds.append(fund_model.PortfolioFund(id=fund_id, quantity=quantity))
        
        db_user.portfolio.initial_investment += db_fund.nav * quantity
        db.commit()
        db.refresh(db_user)
        return db_user.portfolio
    
    raise HTTPException(status_code=404, detail="User or Fund not found")

@router.post("/sell/{user_id}", response_model=PortfolioOut)
def sell_fund(user_id: int, fund_id: int, quantity: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    db_fund = db.query(fund_model.Fund).filter(fund_model.Fund.id == fund_id).first()
    
    if db_user and db_fund:
        fund_in_portfolio = next((f for f in db_user.portfolio.funds if f.id == fund_id), None)
        if fund_in_portfolio and fund_in_portfolio.quantity >= quantity:
            fund_in_portfolio.quantity -= quantity
            db_user.portfolio.initial_investment -= db_fund.nav * quantity
            db.commit()
            db.refresh(db_user)
            return db_user.portfolio
        else:
            raise HTTPException(status_code=400, detail="Insufficient quantity to sell")
    
    raise HTTPException(status_code=404, detail="User or Fund not found")
