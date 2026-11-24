def to_upper(text):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in text:
        found = False
        for i in range(26):
            if ch == lower[i]:
                result = result + upper[i]
                found = True
                break
        if not found:
            result = result + ch

    return result


def show_details(name, age, city):
    city_upper = to_upper(city)
    print("Name:", name)
    print("Age:", age)
    print("City:", city_upper)

    if age < 18:
        print("Minor")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior Citizen")



show_details("Rohan", 22, "pune")
