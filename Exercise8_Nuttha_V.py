print("Please login")
print("-------------------")
usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput =="fruit" and passwordInput =="shop":
    print("-------------------")
    print("Welcome to Fruit Shop")
    print("-------------------")
    print("1" ,"Apple  ","price","35","THB")
    print("2" ,"Coconut","price","50","THB")
    print("3" ,"Durain ","price","90","THB")
    print("4" ,"Grape  ","price","80","THB")
    print("5" ,"Kiwi   ","price","70","THB")
    print("-------------------")
    fruit = int(input("Select number fruit you want :"))
    amount = int(input("How many fruit you want :"))
    if fruit ==1:
        price = 35
        total = price*amount
        print("total price :",total,"THB")
    elif fruit ==2:
        price = 50
        total = price*amount
        print("total price :",total,"THB")
    elif fruit ==3:
        price = 90
        total = price*amount
        print("total price :",total,"THB")
    elif fruit ==4:
        price = 80
        total = price*amount
        print("total price :",total,"THB")
    elif fruit ==5:
        price = 70
        total = price*amount
        print("total price :",total,"THB")
    else:
        print("Please try again")
else:
    print("Please try again")
print("-------------------")
print("Thank you")








