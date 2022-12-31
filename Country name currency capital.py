n=int(input('No of countries needed : '))
dict1=dict()
for i in range(n):
    name=input("Enter the Countrie\'s Name :")
    cap=input("Capital :")
    cur=input("Currency :")
    dict1[name]=cap,cur
print("COUNTRY\tCAPITAL AND CURRENCY")
for i in dict1:
    print(i,"\t\t",dict1[i])
a=input('SEARCH FOR A COUNTRY : ')
print('Country =',a)
print("Capial and Currency =",dict1[a])
