"""Testing the Calculator"""
import unittest
from calculator.calculator import Calculator


def test_calculator_add():
    """Testing the Add function of the calculator """
    """Arrange"""
    value_a = 1
    value_b = 2

    """Act"""
    addition = Calculator.add_number(value_a,value_b)

    """Assert"""
    assert  addition==3


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert  Calculator.subtract_number(1,2)== -1

def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    assert Calculator.multiply_numbers(2,3)== 6

def test_calculator_divide():
    """Testing the divide method of the calculator"""
    assert Calculator.divide_numbers(4,2)== 2




class MyTestCase(unittest.TestCase):
    """A test case is the individual unit of testing.unittest provides a base class"""
    def test_calculator_divide_by_zero(self):
        """Testing the divide method of the calculator when dividing by zero"""
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide_numbers(4,0)
if __name__ == '__main__':
    unittest.main()
