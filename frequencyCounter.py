def freq(s):
    d={}
    s=s.upper().replace(" ","")

    for i in s:
        d[i]=d.get(i,0)+1

    return d

def maxfreq(s):

    d={}
    s=s.upper().replace(" ","")

    for i in s:
        d[i]=d.get(i,0)+1

    maxfrequent=max(d, key=d.get)
    
    return maxfrequent


s=input("Enter Text: ")
d=freq(s)
f=maxfreq(s)
print(f"{f} with frequency: {d.get(f)}")
        
