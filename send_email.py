import smtplib
import ssl
from email.message import EmailMessage
from generate_code import save_code_to_file  # Gera uma nova chave

EMAIL_SENDER = "matrixecho.sp@gmail.com"
EMAIL_PASSWORD = "mafefe4598"
EMAIL_SUBJECT = "Sua Chave de Ativação - Bot de Arbitragem"

def send_email(email_recipient):
    """ Gera uma chave e envia por e-mail """
    key = save_code_to_file()  
    body = f"Olá,\n\nAqui está sua chave de ativação: {key}\n\nAtive o bot com essa chave."

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_SENDER
    msg["To"] = email_recipient

    # Configuração do SMTP para enviar via Gmail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

    print(f"📩 Chave enviada para {email_recipient}!")

# Enviar chave para um cliente
if __name__ == "__main__":
    send_email("cliente@email.com")
