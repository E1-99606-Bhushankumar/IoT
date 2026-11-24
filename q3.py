
num = int(input("Enter a number : "))

d1 = num // 1000
d2 = (num // 100)% 10
d3 = (num // 10) % 10
d4 = num % 10
print(f"face value : {d1} {d2} {d3} {d4}")

print(f"place value  9361 : {d1 * 1000} + {d2 * 100} + { d1 * 10} + {d4}")

print(f"Reverse : {d4}{d3}{d2}{d1}")