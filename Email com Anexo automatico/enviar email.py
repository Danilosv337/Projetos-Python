import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

assunto = "Titulo"
conteudo = "Texto Dentro Do Email"
email_envio = "Email De Envio"
email_destino = "Email Destino"
emails_com_copias=''
senha = 'Senha'

# Cabeçalho
message = MIMEMultipart()
message["From"] = email_envio
message["To"] = email_destino
message["Subject"] = assunto
message["Bcc"] = emails_com_copias  # (Email Com Cc)

# Corpo Do Email
message.attach(MIMEText(conteudo, "plain"))

# No mesmo diretório do programa
arquivo = "Clientes VPN.xlsx"  

# Abrindo Arquivo
with open(arquivo, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    
encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {arquivo}",
)

# adicionando Anexo
message.attach(part)
texto = message.as_string()

# Config Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_envio, senha)
    server.sendmail(email_envio, email_destino, texto)