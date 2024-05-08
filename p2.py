# random generator in python Game
import random
guess=int(input("Guess the number"))
def generate_random(start, end):
    """Generate a random number between start and end (inclusive)."""
    
    
    return random.randint(start, end)
# calling the ramdom function
result=(generate_random(1,  5))

print("the correct number is:",result)
if result==guess: 
  print("Congratulations you Win")
else:
     print("Sorry You Lose")

