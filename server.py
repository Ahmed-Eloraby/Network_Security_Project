import socket

import rsa
import pandas as pd
import smtplib
from email.message import EmailMessage

def send_emails():


    # set your email and password
    # please use App Password
    email_address = "ns-team-20@hotmail.com"
    email_password = "vm6f2Xkk82U8g8X"

    # create email
    msg = EmailMessage()
    msg['Subject'] = "Email subject 2"
    msg['From'] = email_address
    msg['To'] = get_recipient_list()
    msg.set_content("Test")

    # send email
    smtp = smtplib.SMTP('smtp.office365.com', 587 )
    smtp.starttls()
    print('Logging IN')
    smtp.login(email_address, email_password)
    print('Sending Messages')
    smtp.send_message(msg)
    print("Emails Sent Sucessfully")

def get_recipient_list():

    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Wcb2hzqL56QorxwBFW96QWSuyYv_x9VwiFH1nMqJCHA/gviz/tq?tqx=out:csv')

    return df.Email.to_list()

def RSA():
    public_key,private_key=rsa.newkeys(256)
    f = open("keyPair.key", "wb")

    # print(pub)
    # print(pr)
    f.write(public_key.save_pkcs1("PEM"))
    f.write(private_key.save_pkcs1("PEM"))
    # f.write(str2)
    f.close()
    return public_key,private_key



# send_emails()


SERVER_IP = '192.168.1.14'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn,addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:

        # conn.send(b'Hello World')


        public_key, private_key = RSA()
        print(type(public_key))
        conn.send(public_key.save_pkcs1("PEM"))


        aes_key = conn.recv(1024)