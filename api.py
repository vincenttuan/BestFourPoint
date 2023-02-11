from BFP_Service import get_one, query_all
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


@app.get('/bfp/all')
def all():
    return query_all()




