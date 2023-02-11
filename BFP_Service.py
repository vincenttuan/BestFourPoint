from BFP_Dao import find_all, find_one, append_record
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


if __name__ == '__main__':
    print(query_all())
    print(get_one('2330'))
