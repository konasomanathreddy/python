def unit_converter():
    print("1. Km to Miles  2. Celsius to Fahrenheit  3. Kg to Pounds")
    choice = int(input("Choose conversion: "))

    if choice == 1:
        km = float(input("Enter distance in km: "))
        print(f"{km} km = {km * 0.621371:.2f} miles")
    elif choice == 2:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
    elif choice == 3:
        kg = float(input("Enter weight in kg: "))
        print(f"{kg} kg = {kg * 2.20462:.2f} pounds")
    else:
        print("Invalid choice")

unit_converter()