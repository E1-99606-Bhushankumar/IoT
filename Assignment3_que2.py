numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numbers:
    fact = 1
    current = 1
    
    seq = []
    while current <= n:
        seq = seq + [current]
        current = current + 1
        
    for i in seq:
        fact = fact * i
        
    print("Factorial of", n, "is", fact)
