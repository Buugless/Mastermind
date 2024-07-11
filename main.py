import random



def random_number():
    number = random.randrange(1000,10000)
    return number

def status(number,guessed_number):
    display = ""
    print("Your guess: ",guessed_number)
    if str(number)[:1] == str(guessed_number)[:1]:
        display += str(guessed_number)[:1]
    else:
        display += "X"  
    if str(number)[1:2] == str(guessed_number)[1:2]:
        display += str(guessed_number)[1:2]
    else:
        display += "X"  
    if str(number)[2:3] == str(guessed_number)[2:3]:
        display += str(guessed_number)[2:3]
    else:
        display += "X"  
    if str(number)[-1:] == str(guessed_number)[-1:]:
        display += str(guessed_number)[-1:]
    else:
        display += "X"  
     
    return display

def mastermind_game(number,n):
    
   
    ctrl = 1

    print("Number is: ",status(number,n))
    while n != number:
        
        n = int(input("Guess the 4 digit number: "))
        ctrl += 1 
        if n < 1000 or n >10000:
            print("You must enter 4 digit number")
            continue
        if n == number:
            print("You guessed the number! It took you ",ctrl," tries")
        else:
            print("Number is: ",status(number,n))
    return ctrl    

number = random_number()
print(number)
print("Player 1 turn")
n = int(input("Guess the 4 digit number: "))
if n == number:
    print("You guessed the number in the first try. You are a Mastermind")
else:
    player1 = mastermind_game(number,n)
    print("Player 2 turn")
    n = int(input("Guess the 4 digit number: "))
    player2 = mastermind_game(number,n)
    if player1 > player2:
        print("Player 2 won! It took you",player2," tries")
    else:
        print("Player 1 won! It took you",player1," tries")