import smtplib, ssl
import time

ts = time.gmtime()
cryptoTime = time.strftime("%Y-%m-%d %H:%M:%S", ts)
emailSignature = "\n \n Sent by SeanLeitch's CryptoAlert Python Script"
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "" # Email adress from which you will send the alert
password = "" # Password for that email account
receiver_email = ""
messageBuy = """\
Subject: CryptoAlert: BUY ETH NOW

Ethereum has dropped bellow 1600 EUR, now is the time to buy!
\nTime:  """ + cryptoTime + emailSignature
messageSell = """\
Subject: CryptoAlert: SELL ETH NOW 

Ethereum has risen above 2600 EUR, now is the time to sell!
\nTime:  """ + cryptoTime + emailSignature

def sendEmailAlertSell():
    # Create a secure SSL context
    context = ssl.create_default_context()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messageSell)

    print("Email Alert (SELL) sent succsesfully")

def sendEmailAlertBuy():
    context = ssl.create_default_context()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messageBuy)

    print("Email Alert (BUY) sent succsesfully")
