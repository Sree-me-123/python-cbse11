n=int(input("Enter how many terms needed :"))
a,b=0,1
if n==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(n-2):
        print(a+b,end=" ")
        a,b=b,a+b
print()

    
