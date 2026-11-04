import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Addition
    def test_add_positive(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(5, 0), 5)

    # Subtraction
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # Multiplication
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
