import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def send_email(sender_email, password, receiver_email, message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    #sender_email = input("Type your email address and press enter: ")
    #password = input("Type your password and press enter:")
    #receiver_email = input("Type reciever's email address and press enter: ")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Email Id Verification using OTP'
    body = message
    msg.attach(MIMEText(body,'plain'))
    message = msg.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    send_email(sender_email, password, receiver_email, message)
    #send_email()
