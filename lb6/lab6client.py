import smtplib, ssl
import base64

# Zad6

# smtp_server = 'smtp.gmail.com'
# port = 587
# sender = input("Enter sender email address: ")
# password = input("Enter your password: ")
#
# receiver = input("Enter receiver's email address: ")
# message = input("Enter your message: ")
#
# context = ssl.create_default_context()
#
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(sender, password)
#     print("Login successful")
#     server.sendmail(sender, receiver, message)

#===============================================================

# Zad 7

smtp_server = 'smtp.gmail.com'
port = 587
sender = input("Enter sender email address: ")
password = input("Enter your password: ")

receiver = input("Enter receiver's email address: ")
subject = input("Enter subject: ")
message = input("Enter your message: ")

f = open("text.txt", "r")
textfile = f.read()

text_bytes = textfile.encode('ascii')
base64_text = base64.b64encode(text_bytes)

data = f"""\
From: {sender}
To: {receiver}
Subject: {subject}
MIME Version: 1.0
Content-Type: multipart/mixed; boundary=\"sep\"
--sep
{message}
--sep
Content-Type: plain/text; name=\"text.txt\"
Content-Disposition: attachment; filename=\"text.txt\"
Content-Transfer-Encoding: base64
{base64_text}
--sep--"""

print(data)


context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    print("Login successful")
    server.sendmail(sender, receiver, message)