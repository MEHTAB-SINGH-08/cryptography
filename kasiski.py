def repeats(text,n=3):
    d={}
    text="".join(i for i in text.upper() if i.isalpha())
    for i in range (len(text)-n+1):
        t=text[i:i+n]
        if t not in d.keys():
            d[t]=[]
        d[t].append(i)
    d={k:v for k,v in d.items() if len(v)>1}
    return d

def distances(text):
    dic=repeats(text)
    d={}
    for k,v in dic.items():
        d[k]=[v[i+1]-v[i] for i in range (len(v)-1)]
    return d

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def gcd_list(nums):
        a=nums[0]
        for i in range (1,len(nums)):
            a=gcd(a,nums[i])
        return a

def candidate_lengths(text):
    d=distances(text)
    dic={}
    for k,v in d.items():
        dic[k]=gcd_list(v)
    return dic

def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

def factor_candidates(text):
    d=candidate_lengths(text)
    dic={}
    for k,v in d.items():
        dic[k]=factors(v)
    return dic

def factor_votes(text):
    dic=factor_candidates(text)
    d={}
    for v in dic.values():
        for i in v:
            d[i]=d.get(i,0)+1
    return d

def rank_candidates(text, max_len):
    d=factor_votes(text)
    l=[(k,v) for k,v in sorted(d.items(), key=lambda int: (-int[1], int[0])) if k<=max_len ]
    return l


# x={"ABC": 12, "XYZ": 8}


# y=factor_candidates(x)
# print(y)

# z=factor_votes(y)
# print(z)

# print(rank_candidates(z))

        



def IC(text):
    t="".join(i for i in text.upper() if 'A'<=i<='Z')
    if len(t)<=1:
        return 0
    else:
        d={}
        for i in t:
            d[i]=d.get(i,0)+1
        num=0
        for v in d.values():
            num+=v*(v-1)
        den=len(t)*(len(t)-1)
        ic=num/den
        return ic 


def group(text, key_len):
    t="".join(i for i in text.upper() if 'A'<=i<='Z')
    l=[]
    for i in range(key_len):
        s=''
        for j in range(i,len(t),key_len):
            s+=t[j]
        l.append(s)
    return l


def avg_ic(text, key_len):
    l=group(text,key_len)
    l1=[]
    for i in l:
        s=IC(i)
        l1.append(s)
    avg=sum(l1)/len(l1)
    return avg 

def rank_key_lengths_IC(text, max_len):
    d={}
    for i in range(1,max_len+1):
        d[i]=avg_ic(text,i)
    d={k:v for k,v in sorted(d.items(), key= lambda int: -int[1])}
    return d

def analyze_key_lengths(text,max_len):
    fac_votes=rank_candidates(text,max_len)
    return fac_votes

def combined_ranking(text,max_len=None):
    cleaned_len=len("".join(i for i in text.upper() if 'A'<=i<="Z"))
    if max_len is None:
        max_len=cleaned_len//20
    if max_len<0:
        return None
    if max_len==0:
        print("Ciphertext too short / Max Key Length is Zero... Analysis can be Unreliable. Do You want to continue ? (Y/N)")
        choice=input("Enter Choice: ").upper()
        match choice:
            case 'Y':
                if cleaned_len==0:
                    return None
                else:
                    max_len=cleaned_len
            case 'N':
                return None
    elif max_len>cleaned_len:
        max_len=cleaned_len
        if max_len==0:
            return None
    l=analyze_key_lengths(text,max_len)
    d=rank_key_lengths_IC(text,max_len)
    d1={}
    c=1
    kasiski={k1:v1 for (k1,v1) in l}
    for k,v in d.items():
        n=kasiski.get(k,0)
        d1[k]={"kasiski": n ,"kasiski rank":next((i+1 for i,V in enumerate(l) if V[0]==k),0), "ic": v, "ic rank":c}
        c+=1
    return d1




# x=combined_ranking("HELLOWORLD", -2)
# print(x)
# for k,v in x.items():
#     print(f"{k} : {v}")

# x=group("Elq hryx ts ytzqr vy wfcbo vuuue wyopv yb otlmzgg elq knwp at gsi evnwpak, qfpx-qbwsdsq qsdsfe wqdncefwar lug bhr eehlhdca qvaa Qfrnoe’ d.  Myarommhrwc mzbykewqp amg gsi mpnyhabro vmwycsmr qtxov gsef qncvusq elq dvai fvne gmfetip hup ehwnemab tlwazvyi pcjy xa hup jgsy evgqxd ef hup eufstixr.  Gsezyf es Afe, sme fbzqyogp, mf knd xtszzwf zhiydwbfw fsae mz hup wcinovab.  Rlgt hvxi Kcfdedwny vqhhcrqr scsy cap sr vvd lazvoekg vy xts uzwbwglp af epwf zrlzqg vy Vaar, si iof dyddetwqr oj waar yii qbxjafg Zvd vno mzgglpxsq tr twf lfesani - diaymzu jlxqf, jzsp-phcrubt qmdscweos, ppqqbg qpace.  Jsegncmmb ulh ovbdiz hup wuhr, lrp vr lrp Cec lmr elmesq elq hryx fc tpx tse.  Zvd, kuz amg n rvubatrs dlrqk kvel bwyzx’e kvyke oao xtwpv, amjl mvaka seuf clvfsq tr fvr xmpryp, jgfatwtsq lpx hup ozcjwipur, hluzr Jsegncmmb, jss iof eexzrc, wffbykqf, ocsmrrc, ezr slwfse, omp abdx at gsi icev.  Nggg elq hjz sr hupq xwiph fvrci, mzgssguu elq hryx iof mms sazysv szv ewk.  Hlqb ffqyse neys, Bcv dcywip ic elq gvoi rznaw fc nwpak n mvqsmp xtog yihse mpqk gz jxifs eiol elq ovc fmyvyk ubfthq.",5)
# for i in x:
#     print(i)

    

def decrypt_ceaser(C,k):
    p=""
    for i in C:
        p+=chr(65+(((ord(i)-65)-k)%26))
    return p


def chi_ranking(text):
    english_letter_frequency = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.16, 'X': 0.15, 'Q': 0.12,
    'Z': 0.074}
    d1={}
    for i in range(26):
        t=decrypt_ceaser(text,i)
        t_len=len(t)
        freq={}
        for j in t:
            freq[j]=freq.get(j,0)+1
        s=0
        for k in range(26):
            e=t_len*(english_letter_frequency[chr(k+ord('A'))]/100)
            s+=((freq.get(chr(k+ord('A')),0)-e)**2)/e
        d1[chr(i+ord('A'))]=s
    d1={k:v for k,v in sorted(d1.items(), key=lambda int: int[1])}
    return d1

# print(combined_ranking("RIJVSUYVJNRIJVSUYVJNRIJVSUYVJNRIJVSUYVJN"))

# rank=chi_ranking("LXFOPVEFRNHR")
# print(rank)


def get_key(s,key):
    l=group(s,key)
    l1=[list(chi_ranking(i).keys()) for i in l]
    l2=[]
    for i in l1:
        l2.append(i[0])
    k=""
    for i in l2:
        k+=i
    return k 

# print(get_key("RIJVSUYVJNRIJVSUYVJNRIJVSUYVJNRIJVSUYVJN",3))

# print(group("RIJVSUYVJNRIJVSUYVJNRIJVSUYVJNRIJVSUYVJN",3))

# print(combined_ranking("GIYBIBSWAYZCBIBCETOCMEVQOPD"))

one="LGDCFDXTSDFMQHILPXSLELQFVGIDQNCVUSQWIMJRDEZRFXEXZOCEZQUPWFCJLVPHUPSXRFESZSOCMPURQEDARCWICEVIPWAELQTV"
two="PPPGJSMXSPSMXREPRIOYVIPOYZRSHUPRMFEZADCNOXAGPSSAZOPCABQELQJVWPMUROEDYPWSGRFREFVRCIPOOZZQHUPLUZYDFGHG"
three="SIMTGPVZCBYVQANTRQRJLVYOAOFDWTSXMHELZQZRCWFCCAIPPRDMPSNHSARRYKMHRESMGXQSDRVCIOHVZREOAOEZSYOIDZLHSYOA"
four="ASUBGPHFCJLVPHUPQMFXPXZSNCXTSELMXKNJWFOGTSZHUPXAKASEPQULRSSQZZQFGSIKSNCWKSGTXEZVMVMFLCIYOVYIPAHNLFVR"
five="DEYSFSIXJRDWFCBOEXCARXTSJLPXGSTPXSQHMFVFESDWRDSRRVDXMBGAPMQRDWOWRYXUTVNHUGPZZQFVPWMBQAIADYPATCULHEVN"
six="AIPVVDXAFLPZQFLXSDBVYKEIAWMSVGPRFSEPHFVEZYSVGSIFOYWAUBQZAEOAOVQOPSIPHUPXMPYPWIVRCIEHHOIZHFCIMRJCSFSA"
seven="ZXQGNYHBFRAEDSQQSDHUPMDSKLQUBNEMABFDSYSPLQQHBDXGRLXEFVRXEFWPDATWYPSFVRCWESNCGTSQQSDPBZOEOOZYFZNYKGOT"
eight="PQGGVNSDHUPRMHHCEXKBCPPCAXEDYREHMMFELQGGCIQHFMIOOZPFGGLHMFVPLVFGNYHNWPJGXSFDLADXPIBSEDEDFNYKQRSCIEVS"
nine="CYUHBFXEWQPXTSVCHACEDEZRGSIEARWPATOCIMRQCMRHROJDCZELQPNVIDMNEXTSPZVZSEGMEWGZVECSEIZDNFWQRGZPUGGPRFCG"
ten="SIYIFTGUOADATCCWEKSQYIMFGSIRCHYXMWAELQWEXIXCQTIEHELZQZYPHFVEZYSVGSIEEHLVQOAOQULROAUHUELQCEOMZOEJWAIA"
eleven="OWATPZRHSEDEFWBYFKSIPRUBTELQANCOQHFWSIZLPQBHVPHXOZAWMDCPEDSQTRFVRHMZRBHWMBQELQHBHRESGEPQRVYXAWGDJMAV"
twelve="WMMFESCFVZLKACQTRHSFEMSOGTSZPRRMZGJTXTQNCIRIYZFESEGEFWBYVMHUPVFVNYEOQRAXUBTELQTVCWFSKAPMBNEMABNCIESN"
thirteen="CGTSEREFVRCWQJVOIZQRNSYDNCIERVQJQFRYXBCFDMNWYTXUSFLRPQUPGWGJSIFVRCXTSEPWGZGDGMBOPVQDRLXQRNDMZUYPQQOF"
fourteen="FVQARYXYOLMIYWFWIMRVYKQGCPGUOYWCIVRYXTSFLQBZRTWEANWPYCEPSNGRCZMHVZREQNYVQJRLPMDNEXQFAMYFSIPRMZNCKQQB"
fifteen="WPQQGTSZCSYYYPRCWYIFEFQWAEIDDEPXQRJTXTQNCIFVRDXDCARIEHPZROZHDMABFLVQHUZWQGHATAFGPHNMFPZQFNWMZRRAIZRR"
sixteen="YXXWAPWATRGMPSANI"

ciphertext=one+two+three+four+five+six+seven+eight+nine+ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen





print(combined_ranking(ciphertext,15))

print(get_key(ciphertext,10))
print(get_key(ciphertext,5))


