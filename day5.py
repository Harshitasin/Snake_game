print("""

   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                 
                                                 

""")
a=int(input("Enter a 1st number"))
b=int(input("Enter a 2nd number"))
print("="*50)
op=input(""" Press key which you perform
1-> addition
2-> subtraction
3-> multiplication
4-> division\n""")
if op=="1":
    print("Addition Result ", a+b)
elif op=="2":
    print("Subtraction Result ", a-b)
elif op=="3":
    print("Multiply Result ", a*b)
elif op=="4":
    print("division Result ", a/b)
else:
    print("Enter valid number")
