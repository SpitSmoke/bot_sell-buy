import uuid
import json

CODES_FILE = "activation_codes.json"

def generate_activation_code():
    return str(uuid.uuid4())[:8]  # Gera um código único de 8 caracteres

def save_code_to_file(code):
    try:
        with open(CODES_FILE, "r") as f:
            codes = json.load(f)
    except FileNotFoundError:
        codes = {}

    codes[code] = {"activated": False}  # Adiciona código como "não ativado"

    with open(CODES_FILE, "w") as f:
        json.dump(codes, f, indent=4)

    print(f"Código gerado: {code}")

# Gera e salva um novo código de ativação
new_code = generate_activation_code()
save_code_to_file(new_code)
