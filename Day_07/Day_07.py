from Classes.Inetcode07 import Inetcode


def amplifier(phase, input_value):
    return Inetcode("../input", phase, input_value).calc()


output = amplifier(0, 0)
output = amplifier(1, output)
output = amplifier(2, output)
output = amplifier(3, output)
output = amplifier(4, output)
print(output)
