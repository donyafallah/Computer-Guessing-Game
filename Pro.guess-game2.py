import random
a = 1
b = 99
computer_guess = random.randint(a,b)
print(computer_guess)
user_idea = input()
while user_idea != "d" :
    if user_idea == "b":
        a = computer_guess + 1
    elif user_idea == "k" :
        b = computer_guess - 1
    computer_guess = random.randint(a,b)    
    print(computer_guess)
    user_idea = input()
               
