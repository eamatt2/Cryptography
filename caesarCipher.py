
#assumes lowercase
def decrypt(cipherText):
    for shiftNum in range(0, 25):
        decrypt = [] 
        for cipherLetter in cipherText:
            cipherNum = (ord(cipherLetter) - ord('a'))
            plainNum = (cipherNum - shiftNum) % 26 
            plainNum = ord('a') + plainNum  
            plainLetter = chr(plainNum) 
            decrypt.append(plainLetter) 
            plainText = "".join(decrypt) 
        print(plainText)

#Cipher text
cipherText = input("Enter the cipher text: ")
decrypt(cipherText)