def decrypt(text,key):
    p=''
    j=0
    for i in text:
        if 'a'<=i<='z':
            C=ord(i)-ord('a')
            k=ord(key[j])-ord('A')
            p+=chr(((C-k)%26)+ord('a'))
            j=(j+1)%(len(key))
        elif 'A'<=i<='Z':
            C=ord(i)-ord('A')
            k=ord(key[j])-ord('A')
            p+=chr(((C-k)%26)+ord('A'))
            j=(j+1)%(len(key))
        else:
            p+=i
    return p


s=input("Enter Ciphertext: ")
k=input("Enter Key: ").upper()

decpt=decrypt(s,k)
print("Plaintext:",decpt)