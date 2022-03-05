n=int(input("enter no of memory=="))
p=[int(input("enter memory partitions=")) for i in range(n)]
pa=int(input("enter no of process=="))
r=[int(input("enter process allocation==")) for i in range(pa)]
d={}
for i in r:
    max=0
    for j in p:
        if(i<=j and max<j):
            max=j
    #print("max=",max)
    if(max!=0):
        p.remove(max)
        d[i]=max
    else:
        d[i]=0
print(d)
for i in d:
    print(i,"=",d[i],end="\n")
