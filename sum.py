#345=======3+4+5=12
num=int(input("Enter the three digit number"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
print(a+b+c)