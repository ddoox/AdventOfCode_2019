from Classes.Inetcode07 import Inetcode
from itertools import permutations


def amplifier(phase, input_value):
    return Inetcode("../input", phase, input_value).calc()


input_value = 0
max_output = 0
phases = range(0, 5)
phases_perms = permutations(phases)


for test in list(phases_perms):
    output = amplifier(test[0], input_value)
    output = amplifier(test[1], output)
    output = amplifier(test[2], output)
    output = amplifier(test[3], output)
    output = amplifier(test[4], output)
    if output > max_output:
        max_output = output
print(max_output)
