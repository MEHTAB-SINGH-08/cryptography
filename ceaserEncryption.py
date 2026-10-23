s=input("Enter Message: ").lower()
C=""
for x in s:
    if x.isalpha():
        C += chr(97 + (((ord(x)-97) + 3) % 26)) 
    else:
        C+=x
print(C.upper())

