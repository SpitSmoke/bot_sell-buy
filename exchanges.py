import ccxt  # type: ignore
import config

# Instância fixa das exchanges
binance = ccxt.binance({
    'apiKey': config.BINANCE_API_KEY,
    'secret': config.BINANCE_SECRET,
    'enableRateLimit': True,
})

kucoin = ccxt.kucoin({
    'apiKey': config.KUCOIN_API_KEY,
    'secret': config.KUCOIN_SECRET,
    'enableRateLimit': True,
})

# Função genérica para pegar preço de qualquer exchange
def get_price(exchange, symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['ask']
        print(f'Preço de {symbol} na {exchange.id.capitalize()}: {price}')
        return price
    except Exception as e:
        print(f'Erro ao buscar preço em {exchange.id.capitalize()}: {e}')
        return None

# Função para verificar saldo
def get_balance(exchange, asset):
    try:
        balance = exchange.fetch_balance()
        available = balance['free'].get(asset, 0)
        print(f'Saldo disponível de {asset} na {exchange.id.capitalize()}: {available}')
        return available
    except Exception as e:
        print(f'Erro ao buscar saldo em {exchange.id.capitalize()}: {e}')
        return None

# Função para comprar um ativo
def buy_order(exchange, symbol, amount):
    try:
        order = exchange.create_market_buy_order(symbol, amount)
        print(f' Compra realizada na {exchange.id.capitalize()}: {order}')
        return order
    except Exception as e:
        print(f' Erro ao comprar na {exchange.id.capitalize()}: {e}')
        return None

# Função para vender um ativo
def sell_order(exchange, symbol, amount):
    try:
        order = exchange.create_market_sell_order(symbol, amount)
        print(f' Venda realizada na {exchange.id.capitalize()}: {order}')
        return order
    except Exception as e:
        print(f' Erro ao vender na {exchange.id.capitalize()}: {e}')
        return None
