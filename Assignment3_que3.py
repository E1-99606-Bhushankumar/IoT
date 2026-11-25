count = int(input("How many elements do you want to enter? "))
user_list = []

i = 0
while i < count:
    val = input("Enter element: ")
    user_list = user_list + [val]
    i = i + 1

print("Alternate elements are:")
index = 0
for item in user_list:
    if index % 2 == 0:
        print(item)
    index = index + 1
