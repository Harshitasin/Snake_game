import random
num=random.randint(1,100)
guess=int(input("Guess karo"))
count=1
while num!=guess:
    if num>guess:
        print("Sorry! galat guess kiya aur badha")
    else:
        print("Sorry! galat guess kiya aur chhota")
    guess = int(input("Guess karo"))
    count=count+1
else:
    print("yes you are correct")
    print("Atempts:  ",count)


