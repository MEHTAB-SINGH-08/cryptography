def encrypt(text,key):
    C=""
    j=0
    for i in text:
        if 'A'<=i<='Z':
            p=ord(i)-ord('A')
            k=ord(key[j])-ord('A')
            c=(p+k)%26
            C+=chr(c+ord('A'))
            j=(j+1)%(len(key))
        elif 'a'<=i<='z':
            p=ord(i)-ord('a')
            k=ord(key[j])-ord('A')
            c=(p+k)%26
            C+=chr(c+ord('a'))
            j=(j+1)%(len(key))
        else:
            C+=i
    return C


s=input("Enter Text: ")
k=input("Enter Key: ").upper()

print(encrypt(s,k))
