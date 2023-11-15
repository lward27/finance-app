from fastapi import Depends, FastAPI, Query
from fastapi.responses import HTMLResponse
from typing import List, Optional

import yfinance as yf

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/info")
async def get_info(ticker_name: str):
    tick = yf.Ticker(ticker_name)
    return tick.info

@app.get("/history")
async def get_history(ticker_name: str, period: str):
    tick = yf.Ticker(ticker_name)
    hist = tick.history(period=period)
    if hist.empty:
        #TODO: Delete Ticker so next time it isn't included in this process
        return "Ticker Not Found"
    else:
        return hist.to_dict()


    