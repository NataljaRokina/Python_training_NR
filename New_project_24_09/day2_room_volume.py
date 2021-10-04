# # Ask user to input 3 numbers - width, length, height
# # Find the volume of the room
#
# length = input(F"Please enter the length of your room:\n")
# width = input(F"Please enter the width of your room:\n")
# height = input(F"Please enter the height of your room:\n")
#
# length_saved = float(length)
# width_saved = float(width)
# height_saved = float(height)
#
# volume = round(length_saved + length_saved + length_saved, 2)
# print(f"Here is calculated volume of your room - in meters: {volume}")
total = 0

i = 0

while i < 10:

    if i % 2 == 0:

        continue

    total += i

    i += 1

