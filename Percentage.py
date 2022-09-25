Name= input(" Enter your Name\t:")
Eng=int(input("English "))
Mal=int(input("Malayalam "))
Mat=int(input("maths "))
social=int(input("social "))
science= int(input("science "))
total=Eng+Mal+Mat+social+science
maximummark=60
Percentage= (total/maximummark)*100

print("Report card ")
print("-------------\n-------------")
print("Name of the student\t:",Name)
print("Percentage obtained\t:",Percentage)
