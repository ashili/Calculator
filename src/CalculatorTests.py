import unittest
from Calculator import Calculator



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add(self):

        self.assertEqual(self.calculator.add(1, 6), 7)
        self.assertEqual(self.calculator.result, 7)

    def test_sub(self):
        self.assertEqual(self.calculator.subtract(5, 1), 4)
        self.assertEqual(self.calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
