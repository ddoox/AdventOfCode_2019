class Inetcode():

    def __init__(self, input_data, phase_value, input_value, current_index, instructions):  # input data - path
        if instructions == 0:
            swap = []
            with open(input_data, "r") as input_file:
                input_file = input_file.read()
                input_file = input_file.strip().split(",")
                for number in input_file:
                    swap.append(int(number))
            self.input_file = [_ for _ in swap]
        else:
            self.input_file = instructions
        self.input_value = input_value
        self.phase_value = phase_value
        self.opcode_index = int(current_index)
        if current_index == 0:
            self.give_phase = True
        else:
            self.give_phase = False

    def calc(self):
        # self.opcode_index = 0
        opcode_value_str = str(self.input_file[self.opcode_index])
        opcode_value_int = int(opcode_value_str[-1])
        output = 0

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
                param_C = self.input_file[self.opcode_index + 1]
            elif opcode_value_int in [3, 4]:
                param_C = self.input_file[self.input_file[self.opcode_index + 1]]
            elif param_B and param_C:
                param_C = self.input_file[self.opcode_index + 1]
                param_B = self.input_file[self.opcode_index + 2]
            elif param_C:
                param_C = self.input_file[self.opcode_index + 1]
                param_B = self.input_file[self.input_file[self.opcode_index + 2]]
            elif param_B:
                param_C = self.input_file[self.input_file[self.opcode_index + 1]]
                param_B = self.input_file[self.opcode_index + 2]
            else:
                param_C = self.input_file[self.input_file[self.opcode_index + 1]]
                param_B = self.input_file[self.input_file[self.opcode_index + 2]]

            if opcode_value_int in [1, 2, 7, 8]:
                result_index = self.input_file[self.opcode_index + 3]
            elif opcode_value_int in [3, 4]:
                result_index = self.input_file[self.opcode_index + 1]

            if opcode_value_int == 1:
                self.input_file[result_index] = param_B + param_C
            elif opcode_value_int == 2:
                self.input_file[result_index] = param_B * param_C
            elif opcode_value_int == 3:
                if self.give_phase:
                    self.input_file[result_index] = self.phase_value
                    self.give_phase = False
                else:
                    self.input_file[result_index] = self.input_value
            elif opcode_value_int == 4:
                output = self.input_file[result_index]
                self.opcode_index += 2
                opcode_value_str = str(self.input_file[self.opcode_index])
                opcode_value_int = int(opcode_value_str[-1])
                return output, self.opcode_index, opcode_value_int, self.input_file

                # print("output: " + str(output))
                # print("opcode index: " + str(self.opcode_index) + "\n")
            elif opcode_value_int == 5:
                if param_C != 0:
                    self.opcode_index = param_B
                else:
                    self.opcode_index += 3
            elif opcode_value_int == 6:
                if param_C == 0:
                    self.opcode_index = param_B
                else:
                    self.opcode_index += 3
            elif opcode_value_int == 7:
                self.input_file[result_index] = 1 if param_C < param_B else 0
            elif opcode_value_int == 8:
                self.input_file[result_index] = 1 if param_C == param_B else 0

            if opcode_value_int in [1, 2, 7, 8]:
                self.opcode_index += 4
            elif opcode_value_int in [3, 4]:
                self.opcode_index += 2

            opcode_value_str = str(self.input_file[self.opcode_index])
            opcode_value_int = int(opcode_value_str[-1])

        # print(output)
        # return output, self.opcode_index, opcode_value_int
