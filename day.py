#user-input(email and password)
#email="Esolution@gmail.com"
#password="1234"
email=input("Enter your mail id")
password=input("Enter your password")
if email=="Esolution@gmail.com":
  if password=="1234":
    print("Welcome")
  else:
    print("You entered wrong password")
    print("=================================")
    password=input("Again enter the password")
    if password=="1234":
      print("Now you entered the right password")
      print("Welcome")
    else:
      print("Sorry set your password again")