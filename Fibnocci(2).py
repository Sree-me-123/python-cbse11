num = int(input("Enter the number:"))

def fibno(a):
    d1, d2 = 0, 1
    num=a
    count = 0
    if num==0:
        print("Enter a valid number")
    else:
        while count<num:
            print(d1)
            fib=d1+d2
            d1=d2
            d2=fib
            count+=1
fibno(num)
