#Affine Cipher

def encryption(a, b, string):
    res = ""

    for i in string:
        value = (ord(i) - ord("a")) % 26 
        encrypt_Num = (((a * value) + b)) % 26
        encrypt_Letter = chr((encrypt_Num + ord("a")))
        res = res + encrypt_Letter
    return res

def decryption(a, b, string):
    res = ""
    
    for i in string:
        a_inverse = modInverse.get(a)
        value = (ord(i) - ord("a")) % 26
        decrypt_Num = (a_inverse * (value - b)) % 26
        decrypt_Letter = chr((decrypt_Num + ord("a")))
        res = res + decrypt_Letter
    return res

def numberFour(a, b, string):
    res = ""

    for i in string:
        value = (ord(i) - ord("a")) % 26 
        encrypt_Num = (((a * value) + b)) % 26
        encrypt_Letter = chr((encrypt_Num + ord("a")))
        res = res + encrypt_Letter
    return res

decision = input("Do you want to encrypt or decrypt or other: ")
value = input("What is the string we are performing the cipher on: ")
modInverse = { 1: 1, 3: 9, 5: 21, 7: 15, 11: 19, 17: 23, 25: 25, 9: 3, 21: 5, 7: 15, 19: 11, 23: 17 }

if decision == "other":
    a = int(input("what is the vlaue of a: "))
    b = int(input("what is the value of b: "))
    message = numberFour(a, b, value)
    print(message)

elif decision == "encrypt":
    for a in range (0, 26):
        if a == 13 or (a % 2 ) == 0 or a > 25:
            print("a must be coprime with 26 or less than 26")
            continue
        for b in range(0,26):
            encryptionText = encryption(a, b, value)
            print(encryptionText)
else:
    for a in range (0, 26):
        if a == 13 or (a % 2 ) == 0 or a > 25:
            print("a must be coprime with 26 or less than 26")
            continue
        for b in range(0,26):
            decryptionText = encryption(a, b, value)
            print(decryptionText)