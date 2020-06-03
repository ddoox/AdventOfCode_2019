from Classes.Inetcode07 import Inetcode
from itertools import permutations


def amplifier(phase, input_value):
    return Inetcode("../input", phase, input_value).calc()


perms = permutations([0, 1, 2, 3, 4])
max_output = 0

for test in list(perms):
    output = amplifier(test[0], 0)
    output = amplifier(test[1], output)
    output = amplifier(test[2], output)
    output = amplifier(test[3], output)
    output = amplifier(test[4], output)
    if output > max_output:
        max_output = output
print(max_output)
