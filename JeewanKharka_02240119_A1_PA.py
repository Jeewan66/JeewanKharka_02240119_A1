def prime_no(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def Sum_prime():
    lower = int(input("Enter num 1: "))
    upper = int(input("Enter num 2: "))
    sum=0
    for i in range (lower,upper+1):
        if prime_no(i):
            sum+=i
    print("Sum of all prime numbers are: ",sum)


def unit_convert():
    print("1.Meter")
    print("2.feet")
    user=int(input("Enter meter or feet: "))   
    num=int(input("Enter a value: "))
    if user==1:
        meter=num*3.2804
        print(f'Your unit in feet is: {meter}')
    elif user==2:
        feet=num*0.3048
        print(f'Your unit in meter is: {feet}')



def counter():
    user=(input("Enter a word: "))
    count=0
    vowel="AEIOUaeiou"
    for i in user:
        if i.isalpha() and i not in vowel:
            count+=1
    print("Consonant count: ", count) 



    
list_no=[]
def min_max():
    list_no.clear()
    user_input=int(input("Enter total list of number: "))
    for i in range(user_input):
        num=int(input(f"Enter values {i+1}: "))
        list_no.append(num)
    print(list_no)

    print("Minimum: ",min(list_no))
    print("maximun: ",max(list_no))


def palindrome():
    user=input("Enter a string: ")
    user1=user[::-1]
    if user==user1:
        print(f'{user} is a palardome')
    else:
        print(f"{user} is not a paladrome")


def word_count():
    word_list = ["the","was","and"]
    count = {"the":0,"and":0,"was":0}
    file=input("Enter file name: ")
    with open(file, 'r') as f:
        file1=f.read()
        file1=file1.lower()
        words=file1.split()

        for word in words:
            if word=="the":
                count["the"]+=1
            elif word=="and":
                count["and"]+=1
            elif word=="was":
                count["was"]+=1
      
    print(f"word count for 'the' is:{count['the']}")
    print(f"word count for 'was' is:{count['was']}")
    print(f"word count for 'and' is:{count['and']}")






while True:
    print("Menu: ")
    print("1. Prime number sum calculator ")
    print("2. Convert length between meters and feet")
    print("3. Count consonants in a string")
    print("4. Find min and max in a list")
    print("5. Check palindrome")
    print("6. Count occurrences of words in file")
    print("7.Exit")

    user_choice=int(input("Enter your choice: "))
    if user_choice==7:
        print("Exited the program: ")
        break
    if user_choice==1:
        Sum_prime()
    elif user_choice==2:
        unit_convert()
    elif user_choice==3:
        counter()
    elif user_choice==4:
        min_max()

    elif user_choice==5:
        palindrome()
    elif user_choice==6:
        word_count()
       
    else:
        print("invalid")
        break