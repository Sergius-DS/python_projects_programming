# VERSION SERGIO
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


print("welcome to computer game")
playing = input("do you want to play? \n").lower()
if playing not in ["yes", "y"]:
  quit()
  print("it will be in another time")
else:
  print("Okay let us play")
  clear_screen()  # Clear the screen after the initial prompt
  print("Now, we go with the questions\n")

  score = 0
  answer = input("what does cpu stand for? \n")
  if answer.lower() == "central processing unit":
    print("correct")
    score += 1
  else:
    print("incorrect")

  answer = input("what does GPU stand for? \n")
  if answer.lower() == "graphics proccess unit":
    print("correct")
    score += 1
  else:
    print("incorrect")

  answer = input("what does RAM stand for? \n")
  if answer.lower() == "random access memory":
    print("correct")
    score += 1
  else:
    print("incorrect")

  answer = input("what does PSU stand for? \n")
  if answer.lower() == "power supply unit":
    print("correct")
    score += 1
  else:
    print("incorrect")
  
  if score == 4:
    print(f"\nGame over! Congratulation for your EFFORT! Your final score is {score} out of 4.")
  else:
     print(f"\nGame over! \nYour final score is {score} out of 4.")
