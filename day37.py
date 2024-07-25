print("\tDay 37: Sci Fi Name Generator")
print()
def sciFiName():
  firstName = input("What is your first name? \n").strip().capitalize()
  newFirst = firstName[0:3]
  lastName = input("What is your last name? \n").strip().lower()
  newLast = lastName[0:3]
  name = f"{newFirst}{newLast} "
  maidenName = input("What is your mother's maiden name?  \n").capitalize().strip()
  city = input("What city were you born in? \n").strip().lower()
  newCity = city[-3:]
  newMaiden = maidenName[0:2]
  print(f"Your sci-fi name is {name}{newMaiden}{newCity}")

sciFiName()