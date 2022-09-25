import unittest
from calculator import Calculator

myCalc = Calculator()


class TestCalc(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(myCalc.plus(5, 3), 8)
        self.assertEqual(myCalc.plus(-2, 6), 4)
        self.assertEqual(myCalc.plus(1.5, 2.35), 3.85)

    def test_minus(self):
        self.assertEqual(myCalc.minus(4, 2), 2)
        self.assertEqual(myCalc.minus(-5, 1), -6)

    def test_multi(self):
        self.assertEqual(myCalc.multi(3, 3), 9)
        self.assertEqual(myCalc.multi(-2, 5), -10)

    def test_div(self):
        self.assertEqual(myCalc.div(8, 2), 4)
        self.assertEqual(myCalc.div(2, 10), 0.2)


if __name__ == '__main__':
    unittest.main()
