swap = []
with open("input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split(",")
    for number in input_file:
        swap.append(int(number))
input_file = [_ for _ in swap]

input_value = 1
result_index = 0
opcode_index = 0

opcode_value_str = str(input_file[opcode_index])
opcode_value_int = int(opcode_value_str[-1])
output = 0
param_B = 0
param_C = 0

while opcode_value_int in [1, 2, 3, 4]:

    if len(opcode_value_str) == 3:
        param_C = int(opcode_value_str[-3])
        param_B = 0
    elif len(opcode_value_str) == 4:
        param_C = int(opcode_value_str[-3])
        param_B = int(opcode_value_str[-4])
    else:
        param_B = 0
        param_C = 0

    if opcode_value_int in [3, 4] and param_C:
        param_C = input_file[opcode_index + 1]
    elif opcode_value_int in [3, 4]:
        param_C = input_file[input_file[opcode_index + 1]]
    elif param_B and param_C:
        param_C = input_file[opcode_index + 1]
        param_B = input_file[opcode_index + 2]
    elif param_C:
        param_C = input_file[opcode_index + 1]
        param_B = input_file[input_file[opcode_index + 2]]
    elif param_B:
        param_C = input_file[input_file[opcode_index + 1]]
        param_B = input_file[opcode_index + 2]
    else:
        param_C = input_file[input_file[opcode_index + 1]]
        param_B = input_file[input_file[opcode_index + 2]]

    result_index = input_file[opcode_index + 3] if opcode_value_int == 1 or opcode_value_int == 2 else input_file[opcode_index + 1]
    if opcode_value_int == 1:
        input_file[result_index] = param_B + param_C
    elif opcode_value_int == 2:
        input_file[result_index] = param_B * param_C
    elif opcode_value_int == 3:
        input_file[result_index] = input_value
    elif opcode_value_int == 4:
        output = input_file[result_index]
        print("output: " + str(output))
        print("opcode index: " + str(opcode_index) + "\n")
    opcode_index += 4 if opcode_value_int == 1 or opcode_value_int == 2 else 2

    opcode_value_str = str(input_file[opcode_index])
    opcode_value_int = int(opcode_value_str[-1])

print(output)
