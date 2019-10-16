def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print("Total Price",(vatCalculate(float(input("Price ")))))