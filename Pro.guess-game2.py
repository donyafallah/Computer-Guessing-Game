import random
a = 1
b = 99
computer_guess = random.randint(a,b)
print(computer_guess)
user_idea = input("Enter one of these option \t<< 1)bigger \t2)smaller \t3)true >> : ")
while user_idea != "true" :
    if user_idea == "bigger":
        a = computer_guess + 1
    elif user_idea == "smaller" :
        b = computer_guess - 1
    else :
        print("Just choose one of them {not choose anything else!} \t<< 1)bigger \t2)smaller \t3)true >> : ")    
    computer_guess = random.randint(a,b)    
    print(computer_guess)
    user_idea = input("Enter one of these option \t<< 1)bigger \t2)smaller \t3)true >> : ")
print("Congratulations dear Computer!")               
