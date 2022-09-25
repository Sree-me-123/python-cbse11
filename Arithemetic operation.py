# To do +,-,/,* arithemetic operations

a=float(input("enter number 1:"))
b=float(input("enter number 2:"))
op=input("enter any one of the operaters (+,-,/,*):")
if op=="+": 
    print(a,"+",b,"=",a+b)
elif op=="-":
    print(a,"-",b,"=",a-b)
elif op=="/":
    if b==0:
        print("Invalid Operation,Divition by 0 is not possible")
    else:
        print(a,"/",b,"=",a/b)
elif op=="*":
    print(a,"*",b,"=",a*b)
else:
    print("This program is made to do +,-,/,* operations only")
        
