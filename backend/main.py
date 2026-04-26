"""MarielBOT SaaS API - Backend principal."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os

app = FastAPI(title="MarielBOT API", version="1.0.0", description="Trading Bot Marketplace")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

REFERRAL = "sfzsojx8cz"

class Register(BaseModel):
    email: str
    password: str
    referral_code: Optional[str] = "sfzsojx8cz"

class Login(BaseModel):
    email: str
    password: str

@app.get("/")
def root():
    return {"name": "MarielBOT API", "status": "online", "referral": REFERRAL}

@app.get("/marketplace")
def marketplace():
    return {"bots": [
        {"id":"s1","name":"Reversal Keltner + Stoch","winrate":"58%","price":"$9.99/mo"},
        {"id":"s2","name":"Trend Pullback EMA + RSI","winrate":"56%","price":"$9.99/mo"},
        {"id":"s3","name":"Breakout Range","winrate":"54%","price":"$9.99/mo"},
        {"id":"s4","name":"Bollinger Rejection","winrate":"57%","price":"$14.99/mo"},
        {"id":"s5","name":"Momentum Continuation","winrate":"55%","price":"$14.99/mo"},
        {"id":"radical","name":"High Payout Scanner","winrate":"55%","price":"$19.99/mo"}
    ], "referral": REFERRAL}

@app.post("/register")
def register(u: Register):
    return {"success":True,"email":u.email,"referral":REFERRAL,"message":"Compte créé"}

@app.post("/login")
def login(u: Login):
    return {"success":True,"email":u.email}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
