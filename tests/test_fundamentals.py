import unittest

from toolkit import fundamentals


class TestFundamentals(unittest.TestCase):
    def test_swap(self):
        self.assertEqual(fundamentals.swap(1, 2), (2, 1))

    def test_count_sum_factorial(self):
        self.assertEqual(fundamentals.count_digits(12345), 5)
        self.assertEqual(fundamentals.count_digits(0), 1)
        self.assertEqual(fundamentals.summation([1, 2, 3]), 6)
        self.assertEqual(fundamentals.factorial(5), 120)
        self.assertEqual(fundamentals.factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            fundamentals.factorial(-1)

    def test_fibonacci_and_reverse(self):
        self.assertEqual(fundamentals.fibonacci_list(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fundamentals.reverse_number(1234), 4321)
        self.assertEqual(fundamentals.reverse_number(-120), -21)

    def test_base_conversion(self):
        self.assertEqual(fundamentals.convert_base(10, 2), "1010")
        self.assertEqual(fundamentals.convert_base(255, 16), "FF")
        with self.assertRaises(ValueError):
            fundamentals.convert_base(5, 1)

    def test_string_to_number(self):
        self.assertEqual(fundamentals.string_to_number("4096"), 4096)
        self.assertEqual(fundamentals.string_to_number("-7"), -7)
        with self.assertRaises(ValueError):
            fundamentals.string_to_number("12a")


if __name__ == "__main__":
    unittest.main()
