a = input("sentance")
z=(a.split(" "))
b = len(z)
f=[]
d=[]
for i in range(b):
    c=len(z[i])
    if (c%2)==0:
        d.append(z[i])
    print("00")
for i in range(len(d)):
    g=len(d[i])
    f.append(g)

x=f.index(max(f))
print(d[x])

