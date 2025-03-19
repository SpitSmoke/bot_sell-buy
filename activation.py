import json
import os

CODES_FILE = "activation_codes.json"
STATUS_FILE = "activation_status.json"

def check_activation(user_code):
    """ Verifica se o código de ativação é válido e marca como usado """
    try:
        with open(CODES_FILE, "r") as f:
            codes = json.load(f)
    except FileNotFoundError:
        return False

    if user_code in codes and not codes[user_code]["activated"]:
        codes[user_code]["activated"] = True  # Marca como ativado
        with open(CODES_FILE, "w") as f:
            json.dump(codes, f, indent=4)
        
        save_activation_status()  # Salva que o bot foi ativado
        return True
    return False

def save_activation_status():
    """ Salva o estado de ativação para que o bot lembre na próxima vez """
    with open(STATUS_FILE, "w") as f:
        json.dump({"activated": True}, f)

def is_bot_activated():
    """ Verifica se o bot já foi ativado anteriormente """
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            status = json.load(f)
            return status.get("activated", False)
    return False
