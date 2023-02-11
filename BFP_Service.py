import twstock
from BFP_Dao import find_all, find_one, append_record, delete_record
def parse_stock(stock):
    stock = list(stock)
    # print(len(stock), type(stock), stock)
    prices = stock[11]
    prices = prices.strip('[').strip(']')
    prices = prices.split(', ')
    stock[11] = prices

    dates = stock[10]
    dates = dates.strip('[').strip(']').replace('datetime.datetime', '')
    dates = dates.split('), (')
    dates = [item.strip('(') for item in dates]
    stock[10] = dates
    return tuple(stock)


def query_all():
    stocks = find_all()
    stocks = [parse_stock(stock) for stock in stocks]
    return stocks


def get_one(symbol):
    stock = find_one(symbol)
    stock = parse_stock(stock)
    return stock

def add(symbol):
    stock = twstock.Stock(symbol)  # 取得標的物件
    bfp = twstock.BestFourPoint(stock)
    # 刪除紀錄
    delete_record(symbol)
    # 加入資料表
    append_record(symbol, bfp.best_buy_1(), bfp.best_buy_2(), bfp.best_buy_3(), bfp.best_buy_4(), bfp.best_sell_1(),
                  bfp.best_sell_2(), bfp.best_sell_3(), bfp.best_sell_4(),
                  str(stock.date), str(stock.price))

if __name__ == '__main__':
    print(query_all())
    print(get_one('2330'))
    add('2330')
