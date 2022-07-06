import random
import string

ascii = string.punctuation
alphabet = "abcdefghijklmnopqrstuvwxyz" 

my_password="yes"
savedpassword=""
def dispatch(): 
    def generatePass():
        generatedPassword =""
        for i in range(0,9):
           generatedPassword+= alphabet[random.randrange(26)]
           generatedPassword+=ascii[random.randrange(len(ascii))] 
           generatedPassword+="name"
        print(f"{usersName} with password {generatedPassword} has been created")
        dispatch()

    def register():
        global usersName
        global my_password
        global savedpassword
        usersName = input('Du ska registreras. Var vänlig ange ett användarnamn: ')
        if len(usersName):
            passd= input(f"Hi {usersName}, would you like me to create a password for you?:")
            if passd=="yes":
                generatePass()
    
            else:
                password=input(f"Ok {usersName}, enter your own password")
                if len(password):
                    savedpassword= password
                    print(f"your password have been saved, you can now login")
                    dispatch()
            
    def login():
        global usersName
        global my_password
        global savedpassword
        Namn = input("Enter username: ")
        if len(Namn) and Namn == usersName:
            usersPassword  =  input(f"Hi {usersName},enter your password: ")
            if usersPassword == my_password or usersPassword == savedpassword: 
                print(f"Welcome {usersName}, you are logged in")
            else:
                print("wrong password, try again") 
       
        

    
        
    print('Var vill du göra?')
    action=input('Ange ett av tre val: 1. Logga in, 2. Registrera, 3. Avbryta: ')
    if action=="1":
        login()
        
    elif action=="2":
        register()
    elif action=='3':
        print('Tack för besöket, välkommen tillbaka')
        return
    else:
        print('Du måste ange en action')
        dispatch()
dispatch()