import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instanciate_calcualtor(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 6), 7)
        self.assertEqual(calculator.result, 7)

    def test_sub(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(5, 1), 4)
        self.assertEqual(calculator.result, 4)



if __name__ == '__main__':
    unittest.main()
