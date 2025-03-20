import uuid
import json

CODES_FILE = "activation_codes.json"

def generate_activation_code():
    """ Gera um código único de ativação """
    return str(uuid.uuid4())[:8]  

def save_code_to_file():
    """ Gera um novo código e salva no arquivo """
    code = generate_activation_code()

    try:
        with open(CODES_FILE, "r") as f:
            codes = json.load(f)
    except FileNotFoundError:
        codes = {}

    codes[code] = {"activated": False}  # Marca como não ativado

    with open(CODES_FILE, "w") as f:
        json.dump(codes, f, indent=4)

    return code  # Retorna o código gerado

# Gera e retorna um novo código de ativação
if __name__ == "__main__":
    new_code = save_code_to_file()
    print(f"🔑 Código gerado: {new_code}")
