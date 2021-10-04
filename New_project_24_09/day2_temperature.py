# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: farenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision

temperature_Celsius = input(f"Please check what is the temperature outside and write here:\n")
temperature_Celsius_saved = float(temperature_Celsius)
temperature_farenheit = temperature_Celsius_saved * 9/5 + 32
print(f"Here is temperature in farenheit: {temperature_farenheit}")
