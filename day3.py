ip1=input("""Choose the way 
a
b
c
------------------------------------------------------------\n""")
ip1=ip1.lower()
if ip1=="a":
    print("Sorry bhai ye galat rasta h")
elif ip1=="b":
    print("Chalo bhago yha se")
elif ip1=="c":
    print("Aage badho rahi")
    print("Kaho raahi kaise jaoge\n")
    ip2=input("""Chuno
    1- Ek aag ka dariya h
    2- Doosri jalti hui nadi
    3- Wo gufa jisme sher h
    --------------------------------------------------------------""")
    if ip2=="1":
        print("Tu to gya ")
    elif ip2=="2":
        print("Rahi naav taiyar h baitho tumhara swagat h")
        print("There are three boxes ")
        ip3=input("""Choose 1 box
        1- copper
        2- silver
        3- Gold
        ----------------------------------------------------------""")
        if ip3=="1":
            print("Vijay ho ")
            ip4=input("btao khajan chahiya ya nahi######").lower()
            if ip4=="haa":
                print("Bhago tum lalchi ho")
            elif ip4=="nahi":
                print("tum ek dayalu insaan ho ye khajana tumhara hua")
            else:
                print("theek se bolo")
        elif ip3=="2":
            print("hehehe chandi ki lalach me galti kar gye")
        elif ip3=="3":
            print("Sona tumhara nuksaan kar baitha")
        else:
            print("Jao yha se")

    elif ip2=="3":
        print("Sher aaya bhaago !!!!")
else:
    print("Tumhara khel khatam")