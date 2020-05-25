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

# print(wire1)
first = True
intersections = []

for coordinates in uniq_wire1:
    if coordinates in uniq_wire2:
        intersections.append(coordinates)
        temp = abs(coordinates[0]) + abs(coordinates[1])
        if first:
            closest = temp
            first = False
        elif temp < closest:
            closest = temp
            # print("Temp: " + str(closest))

print("True: " + str(closest))

#   -   -   -   Part 2  -   -   -   -#

first = True
min_distance = 0
wire1_distance = 0
wire2_distance = 0

for intersection in intersections:

    for i in range(0, len(wire1)):
        if wire1[i][0] == intersection[0] and wire1[i][1] == intersection[1]:
            wire1_distance = i + 1
    for k in range(0, len(wire2)):
        if wire2[k][0] == intersection[0] and wire2[k][1] == intersection[1]:

            wire2_distance = k + 1

    temp_dist = wire1_distance + wire2_distance
    if first:
        min_distance = temp_dist
        first = False
    elif temp_dist < min_distance:
        min_distance = temp_dist

print(min_distance)



# if wire1[1][0] == intersections[4][0]:
#     print("k")




