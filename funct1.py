def arith(*x):
    sum = a + b
    subt = a - b
    mult = a * b
    print(f"addition is {sum}, subtraction is {subt}, and multiplication is {mult}")
print("This function does arithmetic operations with inputed values")    
a=int(input("enter a number "))
b=int(input(f"enter a lesser number than {a} "))
arith(a,b)

def largest(*numbs):
    
    if a > b and a > c:
        print(f"{a} is the largest")
    elif b > a and b > c:
        print(f"{b} is largest")
    else: 
        print(f"{c} is largest")
print("This next function takes 3 numbers and displays the highest")
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
largest(a,b,c)

def count(*noun):
    
    vowl = 0
    conso = 0
    letters = ""
    others = ""
    for i in range(len(trial)):
        if trial[i] in ['a','e','i','o','u']:
            vowl = vowl + 1
            letters += trial[i] 
            
        else: 
            conso = conso + 1 
            others += trial[i]
            
    print(f"vowels in {trial} are {vowl} and they are {letters}")
    print(f"consonants in {trial} are {conso} and they are {others}")
print("The next function counts the vowels and consonant in an word")
trial= input("enter a word")
count(trial)


def checkIf(userName):
    
    asci = ['#', '$', '%']
    if len(userName):
        for f in asci:
            u = 0
            while u < len(userName):
                if f in userName[u]:
                    print("there is asci symbol in your password")
                    return 
                u += 1
            else:
                print("there are no asci symbols in your password")
                return
    else:
        print("valid passwords please")
        checkIf(list(input("Enter a password: ").strip().split()))
print("This last function check if there are asci symbols in a password")        
password = list(input("Enter a password: ").strip().split())
checkIf(password)


