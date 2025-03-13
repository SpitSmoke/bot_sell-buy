import ccxt # type: ignore

def get_binance_price(symbol):
    binance = ccxt.binance({
        'apiKey': 'iTip94XCRLQStvYpOPfLq1NiimSRB6tJW0Jn0Fjxdvu4ccV8M2D0UjA6TM6r6tbG',   
        'secret': 'ydJqKCCCbOPbMek7ZSOamrtJViG7swZTmSj3yDpnrEjwWkWZRw07nWP8BCPHnmgq', 
    })
    ticker = binance.fetch_ticker(symbol)
    price = ticker['ask']
    print(f'Preço de {symbol} na Binance: {price}')
    return price

def get_kucoin_price(symbol):
    kucoin = ccxt.kucoin({
        'apiKey': '67d246e4817fd6000189e14e',   
        'secret': '53c70839-2761-432f-9e1a-15383062c4bd', 
    })
    ticker = kucoin.fetch_ticker(symbol)
    price = ticker['ask']
    print(f'Preço {symbol} na KuCoin: {price}') 
    return price