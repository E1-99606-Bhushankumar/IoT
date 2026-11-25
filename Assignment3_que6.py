def overlapping(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False


l1 = [10, 20, 30, 40]
l2 = [50, 60, 30, 70]
print("Overlapping:", overlapping(l1, l2))
