def decrypt_ceaser(C,k):
    p=""
    for i in C:
        if 'a'<=i<='z':
            p+=chr(97+(((ord(i)-97)-k)%26))
        elif 'A'<=i<='Z':
            p+=chr(65+(((ord(i)-65)-k)%26))
        else:
            p+=i
    return p

s=input("Enter ciphertext: ")

for k in range(26):
    p=decrypt_ceaser(s,k)
    print(f"key {k:2}:",p)









