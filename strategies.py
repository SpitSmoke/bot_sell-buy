import time
from exchanges import binance, kucoin, get_price, get_balance, buy_order, sell_order

SPREAD_THRESHOLD = 0.005  

# Ativo a ser negociado
SYMBOL = 'BTC/USDT'
ASSET = 'BTC'

def arbitrage_strategy():
    while True:
        try:
            # Obter preços das duas exchanges
            binance_price = get_price(binance, SYMBOL)
            kucoin_price = get_price(kucoin, SYMBOL)

            if binance_price is None or kucoin_price is None:
                print('⚠️ Erro ao obter preços. Pulando esta iteração.')
                time.sleep(5)
                continue

            # Calculando o spread entre as exchanges
            spread = (kucoin_price - binance_price) / binance_price

            print(f'📊 Spread atual: {spread:.5%}')

            # Caso o preço na Binance seja menor, compramos lá e vendemos na KuCoin
            if spread >= SPREAD_THRESHOLD:
                print('🟢 Oportunidade de arbitragem detectada!')

                # Verificando saldo disponível para compra e venda
                usdt_balance_binance = get_balance(binance, 'USDT')
                btc_balance_kucoin = get_balance(kucoin, ASSET)

                if usdt_balance_binance is None or btc_balance_kucoin is None:
                    print('⚠️ Erro ao obter saldo. Pulando esta iteração.')
                    time.sleep(5)
                    continue

                # Definir quantidade para operar
                trade_amount = min(usdt_balance_binance / binance_price, btc_balance_kucoin)

                if trade_amount > 0:
                    print(f'🔄 Executando arbitragem: Comprando {trade_amount:.6f} {ASSET} na Binance e vendendo na KuCoin')
                    buy_order(binance, SYMBOL, trade_amount)
                    sell_order(kucoin, SYMBOL, trade_amount)
                else:
                    print('Saldo insuficiente para arbitragem.')

            else:
                print('Spread abaixo do limite. Nenhuma ação tomada.')

            time.sleep(10)  

        except Exception as e:
            print(f'Erro inesperado: {e}')
            time.sleep(5)

# Executar a estratégia
if __name__ == '__main__':
    arbitrage_strategy()
