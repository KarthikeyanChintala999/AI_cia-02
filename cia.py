global s
s = "SNU_CHENNAI"
global l
l = ["U_CH","CHEN","ENNA","NAI","SNU_"]
global seed
seed = " "
ms = ""
for i in l:
    if((i==s[0:4]) or (i==s[0:3])):
        seed = i
pos = l.index(seed)
if(pos!=0):
    l.remove(seed)
    l.insert(0,seed)

def StringCombinator(s,l,seed):
    fs = ""
    fs = fs + seed
    for i in range(1,5):
        seed = l[i]
        if(seed[0:2]==fs[-2:]):
            if(len(seed)==3):
                fs = fs + seed[-1:]
            elif(len(seed)==4):
                fs = fs + seed[-2:]
    print(fs)
        
StringCombinator(s,l,seed)