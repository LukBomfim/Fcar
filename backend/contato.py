from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

EMAIL = os.getenv('EMAIL')
EMAIL_SENHA = os.getenv('EMAIL_SENHA')

def enviarEmail(dados):

    msg = MIMEText(f'''Nome: {dados.get('nome')}
E-mail: {dados.get('email')}
Telefone: {dados.get('telefone')}
Mensagem: {dados.get('mensagem')}''')
        
    msg['Subject'] = f'Nova mensagem: {dados.get("assunto")}'
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    with smtplib.SMTP_SLL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, EMAIL_SENHA)
        smtp.send_message(msg)