chars = ['a', 'b', 'c', 'd', 'e']
updated_list = []

for ch in chars:
    if ch == 'b':
        updated_list = updated_list + [[1, 2, 3]]
    else:
        updated_list = updated_list + [ch]

print(updated_list)
