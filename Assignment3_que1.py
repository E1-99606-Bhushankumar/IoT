def check_voter(name: str, age: int):
    is_eligible = lambda a: a >= 18
    result = is_eligible(age)
    
    if result:
        print(name, "is eligible to vote.")
    else:
        print(name, "is not eligible to vote.")
        
    return result


check_voter("Amit", 22)
check_voter("Sneha", 16)
check_voter("Rohan", 18)
