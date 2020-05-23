def path(move):     # return all wire coordinates
    x = 0
    y = 0
    path = [[x, y]]
    for instruction in move:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "U":
            for distance in range(0, distance):
                y += 1
                path.append([x, y])
        elif direction == "D":
            for distance in range(0, distance):
                y -= 1
                path.append([x, y])
        if direction == "R":
            for distance in range(0, distance):
                x += 1
                path.append([x, y])
        elif direction == "L":
            for distance in range(0, distance):
                x -= 1
                path.append([x, y])
    return path


moves = []
with open("../input", "r") as input_file:
    input_file = input_file.readlines()
    for line in input_file:
        moves.append(line.strip().split(","))

wire1 = path(moves[0])
wire2 = path(moves[1])

wire1.remove([0, 0])
wire2.remove([0, 0])

uniq_wire1 = set(tuple(row) for row in wire1)
uniq_wire2 = set(tuple(row) for row in wire2)

first = True

for coordinates in uniq_wire1:
    if coordinates in uniq_wire2:
        temp = abs(coordinates[0]) + abs(coordinates[1])
        if first:
            closest = temp
            first = False
        elif temp < closest:
            closest = temp
            print("Temp: " + str(closest))

print("True: " + str(closest))


