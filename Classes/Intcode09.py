class Intcode():

    def __init__(self, input_data, input_value):  # input data - path
        swap = []
        with open(input_data, "r") as input_file:
            input_file = input_file.read()
            input_file = input_file.strip().split(",")
            for number in input_file:
                swap.append(int(number))
        self.input_file = [_ for _ in swap]
        self.input_value = input_value
        self.opcode_index = 0
        self.output = 0
        self.relative_base = 0
        self.opcodes_one_param = [3, 4, 9]
        self.opcodes_two_param = [1, 2, 7 , 8]


    def calc(self):
        opcode_value_str = str(self.input_file[self.opcode_index])
        opcode_value_int = int(opcode_value_str[-1])
        if len(opcode_value_str) == 1:  # 9 != 99
            opcode_value_str = "0" + opcode_value_str

        # while opcode_value_int in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        while opcode_value_str[-2:] in ["01", "02", "03", "04", "05", "06", "07", "08", "09"]:

            if len(opcode_value_str) == 3:
                param_C = int(opcode_value_str[-3])
                param_B = 0
                # param_A = 0
            elif len(opcode_value_str) == 4:
                param_C = int(opcode_value_str[-3])
                param_B = int(opcode_value_str[-4])
                # param_A = 0
            # elif len(opcode_value_str) == 5:  # Probably in future
            #     param_C = int(opcode_value_str[-3])
            #     param_B = int(opcode_value_str[-4])
            #     # param_A = int(opcode_value_str[-5])
            else:
                param_C = 0
                param_B = 0
                # param_A = 0
            params = [param_C, param_B]

            for idx, param in enumerate(params):
                if param == 0: # position mode
                    if idx == 0:
                        param_C = self.input_file[self.input_file[self.opcode_index + 1]]
                    elif opcode_value_int not in self.opcodes_one_param:
                        param_B = self.input_file[self.input_file[self.opcode_index + 2]]
                elif param == 1: # immeditate mode
                    if idx == 0:
                        param_C = self.input_file[self.opcode_index + 1]
                    elif opcode_value_int not in self.opcodes_one_param:
                        param_B = self.input_file[self.opcode_index + 2]
                elif param == 2:  # relative mode
                    if idx == 0:
                        param_C = self.input_file[self.input_file[self.opcode_index + 1] + self.relative_base]
                    elif opcode_value_int not in self.opcodes_one_param:
                        param_B = self.input_file[self.input_file[self.opcode_index + 2] + self.relative_base]

            if opcode_value_int in self.opcodes_two_param:
                result_index = self.input_file[self.opcode_index + 3]
            elif opcode_value_int in self.opcodes_one_param:
                result_index = self.input_file[self.opcode_index + 1]

            if opcode_value_int == 1:
                self.input_file[result_index] = param_B + param_C
            elif opcode_value_int == 2:
                self.input_file[result_index] = param_B * param_C
            elif opcode_value_int == 3:
                self.input_file[result_index] = self.input_value
            elif opcode_value_int == 4:
                # self.output = self.input_file[result_index]
                self.output = param_C
                print("output: " + str(self.output))
                print("opcode index: " + str(self.opcode_index) + "\n")
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
            elif opcode_value_int == 9:
                self.relative_base += param_C

            if opcode_value_int in self.opcodes_two_param:
                self.opcode_index += 4
            elif opcode_value_int in self.opcodes_one_param:
                self.opcode_index += 2

            opcode_value_str = str(self.input_file[self.opcode_index])
            if len(opcode_value_str) == 1:
                opcode_value_str = "0" + opcode_value_str
            opcode_value_int = int(opcode_value_str[-1])

        print(self.output)
