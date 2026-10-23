def freqPercentage(s):

    s="".join(i for i in s if i.isalpha()).upper()
    d={}

    if not s:
        return d
    
    for i in s:
        d[i]=(d.get(i,0)+1)

    for k,v in d.items():
        d[k]=(v/len(s))*100

    return d 

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

def check(s):
    s=s.split()
    common={"THE","AND","IS","HELLO"}
    c=0
    for i in s:
        if i in common:
            c+=1
    return c




s=input("Enter Text: ")
d=freqPercentage(s)

# for k,v in sorted(d.items()):
#     print(f"{k}: {v}%")

if not d:
    print("No Leters Found! ")
else:
    letter=max(d, key=d.get)
    poss="ETAI"
    best_score=0
    best_plaintext=""
    for i in poss:
        k=(((ord(letter)-65)-(ord(i)-65))%26)
        p=decrypt_ceaser(s,k)
        score=check(p)
        print(f"Guess: {letter} --> {i} | Key: {k:2} | Plaintext: {p} | Score: {s}")
        if best_score<score:
            best_score=score
            best_plaintext=p
    print()
    print(f"Best plaintext: {best_plaintext} | Score: {best_score}")

    

