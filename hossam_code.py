
 
def generate_random_128bits_ascii():  
    import string  
    import secrets  

    res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(2))  
    # Print the Secure string with the combonation of letters, digits and punctuation   
    print("Secure random string is : "+ str(res)) 
    return res



# x="tester"
# savekey(x)
import os
aes_key=os.urandom(16)

print(aes_key)

# s = generate_random_128bits_ascii()
# nchars = len(s)
# print(sum(ord(s[byte])<<8*(nchars-byte-1) for byte in range(nchars)))
# print((126<<8)+40)
# while(True):
#     x = input()
#     print(ord(x))

