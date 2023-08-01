import random
from colorama import Fore, Style

# variables

randnum = random.randint(0, 100)
guesses = []

#* while for repeat run
while True:

  #? check input is number or no

  try:
     guess = int(input("Enter your guess: "))
  except ValueError:
     print(Fore.LIGHTYELLOW_EX + "You didn't enter a number" + Fore.RESET)
     continue

  # check guess

  if guess > 100 or guess < 0:
     print(Fore.LIGHTRED_EX + "The Guess Only Between {}0{} and {}100{}".format(Style.BRIGHT, Style.NORMAL, Style.BRIGHT, Style.NORMAL) + Fore.RESET)
  elif guess == randnum:
      print(Fore.LIGHTGREEN_EX + "You Guess The Correct Number! In {}{}{} Times".format(Style.BRIGHT, len(guesses), Style.NORMAL) + Fore.RESET)
      break
  elif len(guesses) <= 0:
     print(Fore.YELLOW + "Wrong Number. {}Try Agin...".format(Fore.RESET))
  elif abs(guess - randnum) < abs(guesses[-1] - randnum):
     print(Fore.GREEN + "You Are Getting Further" + Fore.RESET)
  else:
     print(Fore.RED + "You Are Getting Closer" + Fore.RESET)

  #* add guess in guesses list

  guesses.append(guess)

guesses.clear()