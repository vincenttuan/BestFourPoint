from BFP_Service import get_one
from fastapi import FastAPI
app = FastAPI()

@app.get('/book/{book_id}')
def get_book_by_id(book_id: int):
    return {
        'book_id': book_id
    }


@app.get('/bfp/{symbol}')
def get_stock_by_symbol(symbol: str):
    stock = get_one(symbol)
    return stock



