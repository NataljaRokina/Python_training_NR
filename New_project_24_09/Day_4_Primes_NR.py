input_value = input("Please enter any number: ")
input_value = int(input_value)

if input_value > 1:
    for i in range(2, input_value):
        if (input_value % i) ==0:
            print(input_value, "is not a prime")
            break
    else:
        print("Prime number!")
else:
    print(input_value, "also is not a prime!")
