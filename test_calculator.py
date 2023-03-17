from calculator import Calc
import unittest


class TestCalc(unittest.TestCase):
    def test_addition(self):
        calc_1 = Calc(2, 3)
        calc_2 = Calc(3, -6)
        self.assertEqual(calc_1.add(), 5)
        self.assertEqual(calc_2.add(), -3)

    def test_subtraction(self):
        calc_1 = Calc(2, 3)
        calc_2 = Calc(3, -6)
        self.assertEqual(calc_1.sub(), -1)
        self.assertEqual(calc_2.sub(), 9)

    def test_multiplication(self):
        calc_1 = Calc(2, 3)
        calc_2 = Calc(3, -6)
        self.assertEqual(calc_1.mul(), 6)
        self.assertEqual(calc_2.mul(), -18)


    def test_division(self):
        calc_1 = Calc(6, 3)
        calc_2 = Calc(3, -6)
        self.assertEqual(calc_1.div(), 2)
        self.assertEqual(calc_2.div(), -0.5)

if __name__=="__main__":
    unittest.main()
