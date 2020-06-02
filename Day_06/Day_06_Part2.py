def calculate_indirect_orbits(active_object, orbits):
    object_above = ""
    counter = -1
    while object_above != "COM":

        for idx, item in enumerate(orbits):
            if active_object == item[1]:
                counter += 1
                object_above = item[0]
                active_object = item[0]
    return counter


def calculate_path(active_object, orbits):
    object_above = ""
    path = []
    while object_above != "COM":

        for idx, item in enumerate(orbits):
            if active_object == item[1]:
                object_above = item[0]
                active_object = item[0]
                path.append(object_above)
    return path


objects = []
with open("../input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split("\n")
    for idx, item in enumerate(input_file):
        input_file[idx] = item.split(")")
        objects.append(input_file[idx][1])


you_path = calculate_path("YOU", input_file)
san_path = calculate_path("SAN", input_file)

overlapping = [_ for _ in you_path if _ in san_path]

print(you_path.index(overlapping[0]))
print(san_path.index(overlapping[0]))

print("YOU path: " + str(you_path) + "\nSAN path: " + str(san_path))
print("Distance: " + str(you_path.index(overlapping[0]) + san_path.index(overlapping[0])))

