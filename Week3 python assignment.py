

def calculate_discount(price, discount_percent):
    
    if discount_percent >=20:
        return price- (discount_percent/100*price)
    else:
        return price
print(calculate_discount(price = float(input("Enter the price :" )),discount_percent = float (input("Enter the discount :" ))))
    