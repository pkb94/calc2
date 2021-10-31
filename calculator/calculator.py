""" This is the increment function"""

def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1

class Calculator:
    """ This is the Calculator class"""

    history = []
    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        return value_a + value_b

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return value_a - value_b

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and storing result"""
        return value_a * value_b
