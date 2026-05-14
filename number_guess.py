import random

print("NUMBER GUESSING GAME")
print("1. Enter")
print("2. Exit")

response = int(input("Enter your response: "))
    
if (response == 1):
    print("Welcome to the game!!")
    
    while True:
        print("Choose difficulty:")
        print("1. Easy(1-50)")
        print("2. Medium(1-100)")
        print("3. Hard(1-150)")

        choice = int(input("Enter your choice: "))

        if (choice == 1):
         range = 50
         max_attempts = 8
    
        elif (choice == 2):
         range = 100
         max_attempts = 7
    
        else:
         range = 150
         max_attempts = 6
    
        number = random.randint(1, range)
        attempts = 0
    
        while True:
          guess = int(input("Enter a guess: "))
          attempts += 1

          if attempts >= max_attempts:
            print("Game Over!! You are out of attempts.")
            break 
     
          if guess < number:
            print("Too low!")
        
          elif guess > number:
            print("Too high!")    
    
          else:
            print(f"Correct! You have guessed it in {attempts} attempts.")
            break
 
        replay = input("Play Again? ")

        if replay == "No":
         break
 
        elif replay != "Yes":
         print("Invalid input!!")
         break
     
elif (response == 2):
    print("Thanks for stopping by!!")
    
else:
    print("Invalid response.") 