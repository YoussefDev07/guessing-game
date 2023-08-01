import random

# variables

words = []
random.shuffle(words)
word = words[0]
guess = ""
count = 0
limit = 10
out = False

# game

while guess != word and not(out):
  if count < limit:
    print("Try: " + str(count + 1))
    guess = input("Guesse Word: ")
    count += 1
  else:
    out = True

# game resulte

if out:
  print("You are out of try! Guesse word is: " + str(word))
else:
  print("You Win!")