def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234" :
        return showMenu()
    else:
        print("Please try again")
        return login()
def showMenu():
    print("---Bew Shop---")
    print("Please select menu")
    print("1. Vat Calculate")
    print("2. Price Calculate")
    return menuSelect()
def menuSelect():
    userSelected = int(input("1 or 2 :"))
    if userSelected ==1:
        return vatCalculate(int(input("total price :")))
    elif userSelected ==2:
        return priceCalculate()
    else:
        return showMenu()
def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return print(result)
def priceCalculate():
    price1 = int(input("first product"))
    price2 = int(input("second product"))
    return vatCalculate(price1+price2)
login()