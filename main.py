from fastapi import FastAPI
from typing import List
from datetime import datetime
from pydantic import BaseModel

class Account(BaseModel):
    update_date: datetime
    balance: float
    id: int

class Transaction(BaseModel):
    account_id: int
    amount: float
    date: datetime

class RequestPredict(BaseModel):
    account: Account
    transactions: List[Transaction] = []

class ResponsePredict(BaseModel):
    account_id: int
    predicted_amount: float

app = FastAPI()

@app.post("/predict")
async def root(predict_body: RequestPredict):
    transactions = predict_body.transactions
    account = predict_body.account

    
    ###### Call your prediction function/code here ######
    ######
    ######
    ######
    ######
    ####################################################

    ## Return predicted amount along with account id
    return {"account_id": account.id, "predicted_amount": 0}