from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
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
async def get_history(ticker_name: str, period: str, return_type: str = Query("dict", enum=["dict", "html", "text", "dataframe"])):
    tick = yf.Ticker(ticker_name)
    hist = tick.history(period="1mo")
    if return_type == "dict":
        return hist.to_dict()
    if return_type == "html":
        return HTMLResponse(content=hist.to_html(),status_code=200)
    if return_type == "text":
        return hist.to_string()
    if return_type == "dataframe":
        return hist