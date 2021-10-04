# Ask the user to enter 3 numbers, output them in ascending order.
# Note: for now, we solve this task only with if, elif, else actions.
# There is also a solution using sorting and list structure, which we have not yet seen.

first_number = input(f"Please enter any number:\n")
second_number = input(f"Please enter any number - second time:\n")
third_number = input(f"Please enter any number - once more time:\n")

first_number = float(first_number)
second_number = float(second_number)
third_number = float(third_number)

if first_number < second_number < third_number:
    print(f"{first_number, second_number, third_number}")
elif first_number<third_number<second_number:
    print(first_number, third_number, second_number)
elif second_number< first_number< third_number:
     print(f"{second_number, first_number, third_number}")
elif second_number < third_number > first_number:
         print(second_number, third_number, first_number)
elif third_number<first_number<second_number:
     print(third_number, first_number, second_number)
elif third_number < second_number < first_number:
    print(third_number, second_number, first_number)

else:
    print(f"something wrong!")


