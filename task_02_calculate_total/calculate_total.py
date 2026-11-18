print("<---------calculate total----------->")

def calculate_total(price,quantity):
    total_amount = price*quantity
    return total_amount


price = float(input("enter a price  : "))
quantity = int(input("enter a quantity  : "))


print("your total amount is :",calculate_total(price,quantity))