a=input("Enter the colour of the traffic light in capital letters :\t")
if a!='RED' or 'YELLOW' or 'GREEN':
    print('Enter a vallid signal colour')
def message():
    v=light()
    if v==0:
        print("Stop !")
    if v==1:
        print('Wait till the ight is green')
    if v==2:
        print('Go')
    print("SPEED THRILLS BUT KILLS")
def light():
    if a=='RED':
        return 0
    if a=='YELLOW':
        return 1
    if a=='RED':
        return 2
   
message()

    
        
