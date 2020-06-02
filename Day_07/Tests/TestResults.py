from Classes.Inetcode07 import Inetcode
import unittest


class TestResults(unittest.TestCase):

    @staticmethod
    def amplifier1(phase, input_value):
        return Inetcode("test1", phase, input_value).calc()

    @staticmethod
    def amplifier2(phase, input_value):
        return Inetcode("test2", phase, input_value).calc()

    @staticmethod
    def amplifier3(phase, input_value):
        return Inetcode("test3", phase, input_value).calc()

    def test1(self):
        output = self.amplifier1(4, 0)
        output = self.amplifier1(3, output)
        output = self.amplifier1(2, output)
        output = self.amplifier1(1, output)
        output = self.amplifier1(0, output)
        self.assertEqual(output, 43210)

    def test2(self):
        output = self.amplifier2(0, 0)
        output = self.amplifier2(1, output)
        output = self.amplifier2(2, output)
        output = self.amplifier2(3, output)
        output = self.amplifier2(4, output)
        self.assertEqual(output, 54321)

    def test3(self):
        output = self.amplifier3(1, 0)
        output = self.amplifier3(0, output)
        output = self.amplifier3(4, output)
        output = self.amplifier3(3, output)
        output = self.amplifier3(2, output)
        self.assertEqual(output, 65210)


if __name__ == '__main__':
    unittest.main()
