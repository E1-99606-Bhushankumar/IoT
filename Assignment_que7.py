count = int(input("Enter number of elements: "))
numbers = []

i = 0
while i < count:
    num = float(input("Enter number: "))
    numbers = numbers + [num]
    i = i + 1

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)