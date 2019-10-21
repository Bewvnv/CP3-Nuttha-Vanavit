menuList = []
priceList = []
def showBill():
    print("-----My Food-----")
    for number in range(len(menuList)):
        print(menuList[number],(priceList[number]))
def showPrice():
    total = 0
    print("-----Total Price-----")
    for number in range(len(priceList)):
        total += int(priceList[number])
    print(total+total*7/100)
while True:
    menuName = input("please enter menu :")
    if (menuName.lower() =="exit"):
        break
    else:
        menuPrice = input("price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
showPrice()
