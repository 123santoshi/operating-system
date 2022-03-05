n=int(input("enter no of memory=="))
p=[int(input("enter memory partitions=")) for i in range(n)]
pa=int(input("enter no of process=="))
r=[int(input("enter process allocation==")) for i in range(pa)]
d={}
a=-1
for i in r:
    for j in range(a+1,len(n)):
        if(i<=n[j]):
            d[n[j]]=i
            #n.remove(n[j])
            a=j
            break
for i in d:
    print(i,"=",d[i],end="\n")
