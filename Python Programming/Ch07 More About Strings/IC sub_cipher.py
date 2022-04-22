# Developer: Jack Bowman
# Program: sub_cipher
# Date: 02/23/2022

def main():
    # gets message from user and calls encrypt and decrypt function to encrypt the message then decrypt it
    msg = input('Enter a message you would like to encrypt: ').upper()
    encryptedMsg = encrypt(msg)
    decryptedMsg = decrypt(encryptedMsg)

    print(f'The encrypted message is {encryptedMsg}')
    print(f'The decrypted message is {decryptedMsg}')

# encrypts message with unicode + 5
def encrypt(msg):
    encryptedMsg = ''

    for character in msg:  # encrypts each individual character
        encryptedMsg += chr((ord(character)) + 5)  # changes to unicode and adds 5

    return encryptedMsg

# decrypts encrypted message with unicode - 5
def decrypt(msg):
    decryptedMsg = ''

    for character in msg:
        decryptedMsg += chr((ord(character) - 5))

    return decryptedMsg

if __name__ == '__main__':
    main()