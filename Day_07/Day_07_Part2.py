from Classes.Inetcode07_2 import Inetcode
from itertools import permutations


def amplifier(phase, input_value, current_index, instructions):     # return output, next opcode index, next opcode value int, modified instructions
    return Inetcode("../input", phase, input_value, current_index, instructions).calc()


input_value = 0
max_output = 0
phases = range(5, 10)
phases_perms = permutations(phases)
start_index = 0

# 2984052 too low
# tests working
for phases in list(phases_perms):
    #   -   -   -   Init amps   -   -   -   #
    amp_a = amplifier(phases[0], input_value, start_index, 0)
    amp_b = amplifier(phases[1], amp_a[0], start_index, 0)
    amp_c = amplifier(phases[2], amp_b[0], start_index, 0)
    amp_d = amplifier(phases[3], amp_c[0], start_index, 0)
    amp_e = amplifier(phases[4], amp_d[0], start_index, 0)
    max_output = amp_e[0]

    while True:
        try:
            amp_a = amplifier(phases[0], amp_e[0], amp_a[1], amp_a[3])
            amp_b = amplifier(phases[1], amp_a[0], amp_b[1], amp_b[3])
            amp_c = amplifier(phases[2], amp_b[0], amp_c[1], amp_c[3])
            amp_d = amplifier(phases[3], amp_c[0], amp_d[1], amp_d[3])
            amp_e = amplifier(phases[4], amp_d[0], amp_e[1], amp_e[3])
            output = amp_e[0]
            if output > max_output:
                max_output = output
        except TypeError:
            break

    if output > max_output:
        max_output = output
print(max_output)
