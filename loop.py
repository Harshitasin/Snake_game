x = 2
for i in range(1,9):
    for j in range(1,x):
        print("*",end=" ")
    print()
    if i>=4:
        x-=1
    if i<=3:
        x=x+1