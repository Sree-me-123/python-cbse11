Name=input("Enter Name :")
Tot=float(input("Enter Total Mark :"))
Max=int(input("Enter Maximum Mark :"))

Percentage=(Tot/Max)*100

print("Percentage of Mark",Name,"got =",Percentage)

if Percentage>=90:
    print(Name,"got an A grade")
elif Percentage>=80:
    print(Name,"got a B grade")
elif Percentage>=70:
    print(Name,"got a C grade")
elif Percentage>=60:
    print(Name,"got a D grade")
else:
    print(Name,"Failed")
              
