import time
import os
import json
from exchanges import get_price  # Agora usa get_price() corretamente
from activation import check_activation  # Importa a verificação do código

CONFIG_FILE = "config.json"

def check_existing_keys():
    """ Verifica se as chaves de API já estão salvas no arquivo de configuração """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            api_keys = json.load(file)
            required_keys = ["binance_api_key", "binance_api_secret", "kucoin_api_key", "kucoin_api_secret"]
            return all(api_keys.get(key) for key in required_keys)
    return False

def check_arbitragem(symbol):
    binance_price = get_price("binance", symbol)
    kucoin_price = get_price("kucoin", symbol)

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
        print("✅ Ativado com sucesso!")

        if not check_existing_keys():
            print("❌ Nenhuma API Key encontrada! Configure as chaves na interface antes de iniciar o bot.")
            exit()

        print("🚀 Iniciando o bot...")
        symbol = 'BTC/USDT'
        while True:
            check_arbitragem(symbol)
            time.sleep(10)
    else:
        print("❌ Código inválido ou já utilizado. Encerrando o programa.")
