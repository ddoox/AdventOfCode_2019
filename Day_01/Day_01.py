def calculate_fuel(_mass):
    _mass = int(_mass)
    _mass = _mass - _mass % 3
    _mass = _mass / 3 - 2
    return _mass


file = open("input", "r")
sum = 0


for mass in file:
    fuel_weight = calculate_fuel(mass)
    sum += fuel_weight
    while fuel_weight >= 0:
        fuel_weight = calculate_fuel(fuel_weight)
        if fuel_weight > 0:
            sum += fuel_weight

print(sum)
file.close()
Day