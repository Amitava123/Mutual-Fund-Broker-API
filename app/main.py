from fastapi import FastAPI
from app.api import user_api, portfolio_api

app = FastAPI()

app.include_router(user_api.router)
app.include_router(portfolio_api.router)
