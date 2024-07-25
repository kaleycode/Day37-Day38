letterA = ["a"]
letterB = ["b"]
letterY = ["y"]
letterG = ["g"]
letterP = ["p"]
myString = input("Type something! \n")
for letter in myString:
  if letter.lower() in letterA:
    print('\033[0;31m', end='')
  elif letter.lower() in letterB:
    print('\033[0;34m', end='')
  elif letter.lower() in letterY:
    print('\033[1;33m', end='')
  elif letter.lower() in letterG:
    print('\033[0;32m', end='')
  elif letter.lower() in letterP:
    print('\033[0;35m', end='')
  print(letter, end="")
  print('\033[0m', end='')