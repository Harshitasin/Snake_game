email=input("Enter your mail id")
password=input("Enter your password")
if email=="Esolution@gmail.com" and password=="1234":
  print("welcome")
elif email=="Esolution@gmail.com" and password !="1234":
    print("Wrong password")
    password=input("Enter the password again")
    if password=="1234":
      print("Now you entered the right password")
      print("Welcome")
    else:
      print("Sorry set your password again")
else:
  print("You entered wrong details")