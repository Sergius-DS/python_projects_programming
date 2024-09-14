import random

user_wins = 0
computer_wins = 0

options = ["piedra", "papel", "tijeras"]

while True:
  user_input = input("Escriba piedra/papel/tijeras o 'exit' para salir: ").lower()
  if user_input == "exit":
    break
  if user_input not in options:
    continue
  random_number = random.randint(0, 2)
  computer_pick = options[random_number]
  # piedra:0, papel:1, tijeras:2
  print("La computadora eligió", computer_pick + ".")

  if user_input == "piedra" and computer_pick == "tijeras":
    print("Ganaste!")
    user_wins += 1
    continue
  elif user_input == "papel" and computer_pick == "piedra":
    print("Ganaste!")
    user_wins += 1
    continue
  elif user_input == "tijeras" and computer_pick == "papel":
    print("Ganaste!")
    user_wins += 1
    continue
  elif user_input == computer_pick:
    print("Empate")
    continue
  else:
    print("Perdiste!")
    computer_wins += 1

print("Ganaste", user_wins, "veces.")
print("Perdiste", computer_wins, "veces.")
print("Gracias por jugar!")
