import datetime

#Write a program that asks for and saves a username
person_name = input("What is your name?\n")
print(f"Wow, that is a nice name-  {person_name}")
person_name_saved = person_name
#print(type(my_name))
#Ask a question about the user's age, using the username in the question
age = input(f"How old are you, {person_name_saved}?\n")
print(type(age))
age = int(age)
print(type(age))
hundred_years = int(100 - age)
#Shows in how many years the user will be 100 years old
print(f"You will be 100 years old at {hundred_years}")
currentYear = datetime.datetime.now (). year
year_100 = currentYear + hundred_years
#The program also show the year when the user will be 100 years old
print(f"You will be 100 years old in {year_100}")

