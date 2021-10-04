# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of service over 2 years.
# Task. Ask the user for the amount of the monthly salary and the number of years worked.#
# Calculate the bonus.
# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0).

monthly_salary = input(f"Please enter your salary: \n")
monthly_salary = float(monthly_salary)
years = input(f"Please enter the amount of years you work in the company: \n")
years = float(years)
bonus = monthly_salary * 15/100
bonus_time = years - 2
if years >= 5:
    print(f"If You've worked in the company for at least 2 years - you will get {bonus*bonus_time}")
else:#years < 2:
    print(f"Sorry, no bonus  - bonus will be calculated after 2 years you have worked in our company")