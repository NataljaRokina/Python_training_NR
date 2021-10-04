# i = 1
# while i<=78:
#     print(f"i is{i}") # this line will always happen at least once
#     i += 2
#     if (i ==56):
#         break
#         i+= 2

for n in range(1,21):
    if n%2 == 0: # even numbers have no reminder when divided by 2
        print(f"{n} is even")
    else:
        print(f"{n} is odd")