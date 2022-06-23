choice=choice = input("What do you want to do?\n1. Encrypt a message 2. Decrypt a message \n Enter E or D respectively!")
if choice=='e':
        print("encrypt")
elif choice=="d":
        print("decrypt")
def encrypt():
    message=input("enter the massage you want to encrypt")
    ascii_massage=[ord(char)+3 for char in message]
    encrypt_massage=[chr(char) for char in ascii_massage]
    print(''.join(encrypt_massage))
def decrypt():
    message=input("enter the massage you want to decrypt")
    ascii_massage=[ord(char)-3 for char in message]
    decrypt_massage=[chr(char)for char in ascii_massage]
    print(''.join(decrypt_massage))
encrypt()
decrypt()