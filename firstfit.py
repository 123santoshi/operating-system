n=int(input("enter no of memory=="))
ps=[int(input("enter memory partitions=")) for i in range(n)]
pa=int(input("enter no of process=="))
r=[int(input("enter process allocation==")) for i in range(pa)]
d={}
for i in ps:
    for j in r:
        if(i>=j):
            d[i]=j
            r.remove(j)
            break
for i in ps:
    if i not in d.keys():
        d[i]=0
for i in d:
    print(i,"==>",d[i],end="\n")
