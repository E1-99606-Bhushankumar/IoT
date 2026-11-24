call = int(input("Enter number of calls: "))

if call <= 100:
    charge = 200
elif call <= 150:
    charge = 200 + (call - 100) * 0.60
elif call <= 200:
    charge = 200 + (50 * 0.60) + (call - 150) * 0.50
else:
    charge = 200 + (50 * 0.60) + (50 * 0.50) + (call - 200) * 0.40

print(f"Charge: {charge:.2f}")
