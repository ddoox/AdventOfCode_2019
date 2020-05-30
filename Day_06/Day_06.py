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


objects = []
with open("../input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split("\n")
    for idx, item in enumerate(input_file):
        input_file[idx] = item.split(")")
        objects.append(input_file[idx][1])

direct_orbits = idx + 1
indirect_orbits = 0

for item in objects:
    indirect_orbits += calculate_indirect_orbits(item, input_file)

print(indirect_orbits + direct_orbits)

