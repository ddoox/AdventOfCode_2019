# input_file = [1,1,1,4,99,5,6,0,99]
swap = []
with open("input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split(",")
    for number in input_file:
        swap.append(int(number))
input_file = swap.copy()

result = 0
found = False

for noun in range(0, 100):
    for verb in range(0, 100):
        input_file = swap.copy()
        input_file[1] = noun
        input_file[2] = verb
        result_index = 0
        opcode = 0

        while input_file[opcode] == 1 or input_file[opcode] == 2:
            if input_file[opcode] == 1:
                result_index = input_file[opcode + 3]
                input_file[result_index] = input_file[input_file[opcode + 1]] + input_file[input_file[opcode + 2]]
                opcode += 4
            if input_file[opcode] == 2:
                result_index = input_file[opcode + 3]
                input_file[result_index] = input_file[input_file[opcode + 1]] * input_file[input_file[opcode + 2]]
                opcode += 4
            if input_file[0] == 19690720:
                result = noun * 100 + verb
print(result)
