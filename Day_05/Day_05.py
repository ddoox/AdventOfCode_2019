input_file = [3, 0, 4, 0, 99]
swap = []
with open("input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split(",")
    for number in input_file:
        swap.append(int(number))
input_file = swap.copy()

# 36312386 - bad

input_value = 1
result_index = 0
opcode_index = 0
# opcode_index = 182
# opcode_index = 10
# opcode_index = 12
# opcode_index = 58
# opcode_index = 80
# opcode_index = 102
# opcode_index = 126
# opcode_index = 150
# opcode_index = 206
# opcode_index = 220
previous_opcode = 0

opcode_value_str = input_file[opcode_index].__str__()
opcode_value_int = int(opcode_value_str[opcode_value_str.__len__() - 1])
output = 0
param_B = 0
param_C = 0

while opcode_value_int == 1 or opcode_value_int == 2 or opcode_value_int == 3 or opcode_value_int == 4:

    if opcode_value_str.__len__() == 3:
        param_C = int(opcode_value_str[opcode_value_str.__len__() - 3])
    elif opcode_value_str.__len__() == 4:
        param_C = int(opcode_value_str[opcode_value_str.__len__() - 3])
        param_B = int(opcode_value_str[opcode_value_str.__len__() - 4])
    else:
        param_B = 0
        param_C = 0

    if opcode_value_int in [3, 4] and param_C:
        param_C = input_file[opcode_index + 1]
    elif opcode_value_int in [3, 4]:
        param_C = input_file[input_file[opcode_index + 1]]
    elif param_B and param_C:
        param_B = input_file[opcode_index + 1]
        param_C = input_file[opcode_index + 2]
    elif param_C:
        param_B = input_file[input_file[opcode_index + 2]]
        param_C = input_file[opcode_index + 1]
    elif param_B:
        param_B = input_file[opcode_index + 2]
        param_C = input_file[input_file[opcode_index + 1]]
    else:
        param_C = input_file[input_file[opcode_index + 1]]
        param_B = input_file[input_file[opcode_index + 2]]

    if opcode_value_int <= 2:
        result_index = input_file[opcode_index + 3]
        if opcode_value_int == 1:
            input_file[result_index] = param_B + param_C
        else:
            input_file[result_index] = param_B * param_C
        opcode_index += 4
    elif opcode_value_int <= 4:
        result_index = input_file[opcode_index + 1]
        if opcode_value_int == 3:
            input_file[result_index] = input_value
        else:
            output = input_file[result_index]
            print("output: " + str(output))
            print("opcode index: " + str(opcode_index))
            print("pre index: " + str(previous_opcode) + "\n")
        opcode_index += 2

    previous_opcode = opcode_index
    opcode_value_str = input_file[opcode_index].__str__()
    opcode_value_int = int(opcode_value_str[opcode_value_str.__len__() - 1])
    # print(input_file)


print(output)
