quantity = int(input("Enter quantity: "))
unit_price = 5
total_price = quantity * unit_price

if quantity > 50:
    discount = total_price * 0.15
elif quantity > 30:
    discount = total_price * 0.10
else:
    discount = 0

final_price = total_price - discount
print("Total Price after discount: Rs", final_price)