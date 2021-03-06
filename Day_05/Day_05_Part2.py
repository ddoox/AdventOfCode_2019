swap = []
with open("input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split(",")
    for _ in input_file:
        swap.append(int(_))
input_file = [_ for _ in swap]

input_value = 5
result_index = 0
opcode_index = 0

opcode_value_str = str(input_file[opcode_index])
opcode_value_int = int(opcode_value_str[-1])
output = 0
param_B = 0
param_C = 0

while opcode_value_int in [1, 2, 3, 4, 5, 6, 7, 8]:

    if len(opcode_value_str) == 3:
        param_C = int(opcode_value_str[-3])
        param_B = 0
        # param_A = 0
    elif len(opcode_value_str) == 4:
        param_C = int(opcode_value_str[-3])
        param_B = int(opcode_value_str[-4])
        # param_A = 0
    elif len(opcode_value_str) == 5:
        param_C = int(opcode_value_str[-3])
        param_B = int(opcode_value_str[-4])
        # param_A = int(opcode_value_str[-5])
    else:
        param_C = 0
        param_B = 0
        # param_A = 0

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

    if opcode_value_int in [1, 2, 7, 8]:
        result_index = input_file[opcode_index + 3]
    elif opcode_value_int in [3, 4]:
        result_index = input_file[opcode_index + 1]

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
    elif opcode_value_int == 5:
        if param_C != 0:
            opcode_index = param_B
        else:
            opcode_index += 3
    elif opcode_value_int == 6:
        if param_C == 0:
            opcode_index = param_B
        else:
            opcode_index += 3
    elif opcode_value_int == 7:
        input_file[result_index] = 1 if param_C < param_B else 0
    elif opcode_value_int == 8:
        input_file[result_index] = 1 if param_C == param_B else 0

    if opcode_value_int in [1, 2, 7, 8]:
        opcode_index += 4
    elif opcode_value_int in [3, 4]:
        opcode_index += 2


    opcode_value_str = str(input_file[opcode_index])
    opcode_value_int = int(opcode_value_str[-1])

print(output)
