def calculate_salary():
    basic = 30000
    hra = basic * 20 / 100
    da = basic * 10 / 100
    gross = basic + hra + da

    if gross > 50000:
        bonus = gross * 5 / 100
    else:
        bonus = gross * 2 / 100

    final_salary = gross + bonus

    print("Basic Salary:", basic)
    print("Gross Salary:", gross)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)



calculate_salary()
