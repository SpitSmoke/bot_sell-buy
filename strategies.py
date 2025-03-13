import time
from exchanges import get_binance_price, get_kucoin_price  # Importando as funções atualizadas

def check_arbitrage(symbol='BTC/USDT'):
    price_binance = get_binance_price(symbol) 
    price_kucoin = get_kucoin_price(symbol)    

    if price_binance > price_kucoin:
        print(f'Compre na KuCoin por {price_kucoin} e venda na Binance por {price_binance}')
    else:
        print(f'Compre na Binance por {price_binance} e venda na KuCoin por {price_kucoin}')

    spread = (price_binance - price_kucoin) / price_kucoin * 100  

    print(f'Spread: {spread:.2f}%')

if __name__ == '__main__':
    check_arbitrage()
    time.sleep(10)
