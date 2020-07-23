password = str(input("Enter Password: "))

invalid = True
#Must run in a loop until the user enters a valid password
while invalid:
  isValid = 0
  password = str(input("create a password: "))

  #The password must be [8,16] characters long.
  if len(password) > 8 and len(password) < 16:
    isValid+=1
  #The password must have at least one upper case letter and one lower case letter.