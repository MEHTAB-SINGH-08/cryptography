s=input("Enter Code: ").upper()
p=""
for x in s:
    if x.isalpha():
        p+=chr(65 + (((ord(x) - 65) - 3) % 26))
    else:
        p+=x
print(p.lower())