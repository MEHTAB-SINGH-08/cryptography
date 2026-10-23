def encrypt(text,key):
    C=""
    j=0
    if not key.isalpha():
        print("Invalid Key.")
    else:
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


def decrypt(text,key):
    p=''
    j=0
    if not key.isalpha():
        print("Invalid Key.")
    else:
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


c1=encrypt("ATTACKATDAWN","LEMON")
p1=decrypt(c1,"LEMON")
c2=encrypt("Hello, World!","Key")
p2=decrypt(c2,"Key")
c3=encrypt("XYZ abc!","dog")
p3=decrypt(c3,"dog")

print(c1,"\t",p1)
print(c2,"\t",p2)
print(c3,"\t",p3)

