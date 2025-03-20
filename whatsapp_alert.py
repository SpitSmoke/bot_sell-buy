import os

def send_whatsapp_message(phone_number, message):
    """ Envia uma mensagem para o WhatsApp usando yowsup """
    command = f"yowsup-cli demos -s {phone_number} \"{message}\""
    os.system(command)

# Teste enviando uma mensagem para seu próprio número
if __name__ == "__main__":
    send_whatsapp_message("41933003310", "🚨 Teste de mensagem do bot de arbitragem!")
