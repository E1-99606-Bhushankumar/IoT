vowels = ['a', 'e', 'i', 'o', 'i', 'u']
target = 'e'
index = 0

for v in vowels:
    if v == target:
        print("Index of", target, "is:", index)
        break
    index = index + 1