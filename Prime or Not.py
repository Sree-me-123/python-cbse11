x=int(input("enter a number"))
p=0
for i in range(2,x-1):
    if x%i==0:
        p=1

if p==1:
    print(x,"is not a Prime number")
else:
    print(x,"is a prime number")


    
        

    
