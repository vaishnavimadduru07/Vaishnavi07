def temperature_modeling(a, b, c, time):
    temperature = a * time**2 + b * time + c
    return temperature

a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10

print("Hard-coded Variables for Weather Modeling")
time_hardcoded = 5
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
print("\n")

print("Keyboard Input for Weather Modeling")
a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))
time_keyboard = float(input("Enter time in hours: "))
print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
print("\n")

print("Read from a File for Weather Modeling")
with open('weather.txt', 'r') as file:
    lines = file.readlines()
    a_file, b_file, c_file, time_file = map(float, lines[0].split())
    print("Temperature for file input coefficients at time", time_file, "hours:", temperature_modeling(a_file, b_file, c_file, time_file))
print("\n")