# Ask user for their temperature.#
# If the user enters below 35, then output "not too cold"#
# If 35 to 37 (inclusive), output "all right"
# If the temperature  over 37, then output  "possible fever"

cold_temperature = input(f"Please enter here your temperature:\n")
cold_temperature_saved = int(cold_temperature)
if cold_temperature_saved < 35:
    print("not too cold")
elif cold_temperature_saved >= 35 and cold_temperature_saved <= 37:
    print("all right")
else:
    print("possible fever")