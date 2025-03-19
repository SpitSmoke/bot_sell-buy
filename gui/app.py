import sys
import threading
import time
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QMessageBox
from PyQt6.QtCore import QTimer
from exchanges import get_price
from activation import check_activation, is_bot_activated  # Importa função que verifica ativação

PAIR = "BTC/USDT"
CONFIG_FILE = "config.json"

class BotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.activated = False  

        if is_bot_activated():
            self.activated = True
            self.initUI(bot_activated=True)
        else:
            self.initUI(bot_activated=False)

    def initUI(self, bot_activated):
        self.setWindowTitle('Bot de Arbitragem')
        self.setGeometry(100, 100, 400, 450)

        self.layout = QVBoxLayout()

        if bot_activated:
            self.load_main_interface()
        else:
            self.label_activation = QLabel('🔐 Digite seu código de ativação:', self)
            self.input_activation = QLineEdit(self)
            self.button_activate = QPushButton('Ativar', self)
            self.button_activate.clicked.connect(self.activate_bot)

            self.layout.addWidget(self.label_activation)
            self.layout.addWidget(self.input_activation)
            self.layout.addWidget(self.button_activate)

        self.setLayout(self.layout)

    def load_main_interface(self):
        """ Substitui a tela de ativação pela interface principal do bot """
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        self.label_status = QLabel('Status: Desligado', self)
        self.label_binance = QLabel('Binance: Carregando...', self)
        self.label_kucoin = QLabel('KuCoin: Carregando...', self)

        self.api_keys_loaded = self.check_existing_keys()

        # Criar campos para API Keys
        self.input_binance_key = QLineEdit(self)
        self.input_binance_key.setPlaceholderText("Binance API Key")

        self.input_binance_secret = QLineEdit(self)
        self.input_binance_secret.setPlaceholderText("Binance API Secret")
        self.input_binance_secret.setEchoMode(QLineEdit.EchoMode.Password)  

        self.input_kucoin_key = QLineEdit(self)
        self.input_kucoin_key.setPlaceholderText("KuCoin API Key")

        self.input_kucoin_secret = QLineEdit(self)
        self.input_kucoin_secret.setPlaceholderText("KuCoin API Secret")
        self.input_kucoin_secret.setEchoMode(QLineEdit.EchoMode.Password)  

        self.button_save_keys = QPushButton('Salvar API Keys', self)
        self.button_save_keys.clicked.connect(self.save_keys)

        self.button_edit_keys = QPushButton('Alterar API Keys', self)
        self.button_edit_keys.clicked.connect(self.show_api_key_fields)
        self.button_edit_keys.hide()  

        if self.api_keys_loaded:
            self.hide_api_key_fields()  

        self.button_start = QPushButton('Iniciar Bot', self)
        self.button_stop = QPushButton('Parar Bot', self)
        self.button_start.clicked.connect(self.start_bot)
        self.button_stop.clicked.connect(self.stop_bot)

        self.log_box = QTextEdit(self)
        self.log_box.setReadOnly(True)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_prices)
        self.timer.start(5000)

        self.layout.addWidget(self.label_status)
        self.layout.addWidget(self.label_binance)
        self.layout.addWidget(self.label_kucoin)
        self.layout.addWidget(self.input_binance_key)
        self.layout.addWidget(self.input_binance_secret)
        self.layout.addWidget(self.input_kucoin_key)
        self.layout.addWidget(self.input_kucoin_secret)
        self.layout.addWidget(self.button_save_keys)
        self.layout.addWidget(self.button_edit_keys)
        self.layout.addWidget(self.button_start)
        self.layout.addWidget(self.button_stop)
        self.layout.addWidget(self.log_box)

    def update_prices(self):
        """ Atualiza os preços das exchanges na interface """
        price_binance = get_price("binance", PAIR)
        price_kucoin = get_price("kucoin", PAIR)

        if price_binance:
            self.label_binance.setText(f'Binance: ${price_binance:.2f}')
        else:
            self.label_binance.setText('Binance: Erro ao buscar preço')

        if price_kucoin:
            self.label_kucoin.setText(f'KuCoin: ${price_kucoin:.2f}')
        else:
            self.label_kucoin.setText('KuCoin: Erro ao buscar preço')

    def log_message(self, message):
        """ Exibe mensagens de log na interface """
        self.log_box.append(message)

    def start_bot(self):
        """ Inicia o bot se estiver ativado """
        if self.activated:
            self.label_status.setText('Status: Rodando...')
            self.log_message("Bot iniciado!")
            self.bot_running = True
            self.bot_thread = threading.Thread(target=self.run_bot, daemon=True)
            self.bot_thread.start()
        else:
            QMessageBox.warning(self, "Erro", "❌ Ative o bot primeiro.")

    def stop_bot(self):
        """ Para o bot """
        if self.activated:
            self.label_status.setText('Status: Parado')
            self.log_message("Bot parado.")
            self.bot_running = False
        else:
            QMessageBox.warning(self, "Erro", "❌ Ative o bot primeiro.")

    def run_bot(self):
        """ Simulação de execução do bot (substituir pela lógica real) """
        while self.bot_running:
            self.log_message("Bot verificando arbitragem...")
            time.sleep(10)


def run_gui():
    app = QApplication(sys.argv)
    window = BotApp()
    window.show()
    sys.exit(app.exec())