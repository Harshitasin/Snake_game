#menu driven calculator
#operation -> +,-,*,/,**,//,%
#first num second num
print("""
 _____ _                 _                  _            _       _             
/  ___(_)               | |                | |          | |     | |            
\ `--. _ _ __ ___  _ __ | | ___    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 `--. \ | '_ ` _ \| '_ \| |/ _ \  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
/\__/ / | | | | | | |_) | |  __/ | (_| (_| | | (__| |_| | | (_| | || (_) | |   
\____/|_|_| |_| |_| .__/|_|\___|  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                  | |                                                          
                  |_|                                                          
                                                                                                                                  
""")
op=input("""Enter the operation which you want to perform\n
+ ->    Addition
- ->    Subtraction
* ->    Multiplication
/ ->    Division
\n""")
a=int(input("Enter the first number"))
b=int(input("Enter the Second number"))
if op=="+":
    print("Your addition is", a+b)
elif op=="-":
    print("Your subtraction is ", a-b)
elif op=="*":
    print("Your multiplication is ", a * b)
elif op=="/":
    print("Your division is ", a / b)
else:
    print("Enter valid operator")

