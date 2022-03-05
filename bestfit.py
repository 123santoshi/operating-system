n=int(input("enter no of memory=="))
p=[int(input("enter memory partitions=")) for i in range(n)]
pa=int(input("enter no of process=="))
r=[int(input("enter process allocation==")) for i in range(pa)]
d={i:"0" for i in p}
for i in r:
    for j in p:
        if(i<=j):
            d[j]=i
            p.remove(j)
            break

for i in d:
    print(i,"=",d[i],end="\n")