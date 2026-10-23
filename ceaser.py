def encrypt_ceaser(p,k):
    C=""
    for i in p:
        if 'a'<=i<='z':
            C+=chr(97+(((ord(i)-97)+k)%26))
        elif 'A'<=i<='Z':
            C+=chr(65+(((ord(i)-65)+k)%26))
        else:
            C+=i
    return C

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

s=input("Enter plaintext: ")

print(decrypt_ceaser(s,3))
for k in range(26):
    C=encrypt_ceaser(s,k)
    p=decrypt_ceaser(C,k)

    assert p==s, f"Test failed by key {k}"

print("All went well!")


