from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

EMAIL = os.getenv('EMAIL')
EMAIL_SENHA = os.getenv('EMAIL_SENHA')

def enviarEmail(dados):

    msg = MIMEText(f'''Nome: {dados.get('nome')}\n
E-mail: {dados.get('email')}\n
Telefone: {dados.get('telefone')}\n
Mensagem: {dados.get('mensagem')}''')
        
    msg['Subject'] = f'Nova mensagem: {dados.get("assunto")}'
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, EMAIL_SENHA)
        smtp.send_message(msg)