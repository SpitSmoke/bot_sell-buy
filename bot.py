import time
from exchanges import get_binance_price, get_kucoin_price
from activation import check_activation  # Importa a verificação do código

def check_arbitragem(symbol):
    binance_price = get_binance_price(symbol)
    kucoin_price = get_kucoin_price(symbol)

    if binance_price and kucoin_price:
        spread = ((kucoin_price - binance_price) / binance_price) * 100
        print(f'\n[INFO] {symbol} Prices:')
        print(f'Binance: {binance_price:.2f}')
        print(f'KuCoin: {kucoin_price:.2f}')
        print(f'Spread: {spread:.2f}%\n')
    else:
        print(f'[ERROR] Failed to fetch prices')

if __name__ == '__main__':
    user_code = input("🔐 Digite seu código de ativação: ")

    if check_activation(user_code):
        print("✅ Ativado com sucesso! Iniciando o bot...")
        symbol = 'BTC/USDT'
        while True:
            check_arbitragem(symbol)
            time.sleep(10)
    else:
        print("❌ Código inválido ou já utilizado. Encerrando o programa.")
