import ccxt
import json
from crypto_utils import decrypt_data

CONFIG_FILE = "config.json"

def load_api_keys():
    """ Carrega as API Keys do arquivo config.json """
    try:
        with open(CONFIG_FILE, "r") as f:
            encrypted_keys = json.load(f)

        return {
            "binance_api_key": decrypt_data(encrypted_keys["binance_api_key"]),
            "binance_api_secret": decrypt_data(encrypted_keys["binance_api_secret"]),
            "kucoin_api_key": decrypt_data(encrypted_keys["kucoin_api_key"]),
            "kucoin_api_secret": decrypt_data(encrypted_keys["kucoin_api_secret"]),
        }
    except FileNotFoundError:
        print("[ERRO] Nenhuma API Key configurada.")
        return None

def get_price(exchange_name, symbol):
    """ Busca o preço da criptomoeda na exchange escolhida """
    api_keys = load_api_keys()
    if not api_keys:
        print("[ERRO] Nenhuma API Key configurada. Configure na interface primeiro.")
        return None

    try:
        if exchange_name == "binance":
            exchange = ccxt.binance({
                "apiKey": api_keys.get("binance_api_key"),
                "secret": api_keys.get("binance_api_secret")
            })
        elif exchange_name == "kucoin":
            exchange = ccxt.kucoin({
                "apiKey": api_keys.get("kucoin_api_key"),
                "secret": api_keys.get("kucoin_api_secret")
            })
        else:
            raise ValueError(f"Exchange '{exchange_name}' não suportada")

        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']

    except Exception as e:
        print(f'Erro ao buscar preço em {exchange_name.capitalize()}: {e}')
        return None
