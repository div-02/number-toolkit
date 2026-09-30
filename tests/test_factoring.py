import math
import unittest

from toolkit import factoring


class TestFactoring(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(factoring.square_root(2), math.sqrt(2), places=6)
        self.assertAlmostEqual(factoring.square_root(0.25), 0.5, places=6)
        with self.assertRaises(ValueError):
            factoring.square_root(-4)

    def test_divisor_and_gcd(self):
        self.assertEqual(factoring.smallest_divisor(91), 7)
        self.assertEqual(factoring.smallest_divisor(13), 13)
        self.assertEqual(factoring.gcd(48, 18), 6)
        self.assertEqual(factoring.gcd(7, 0), 7)

    def test_primes(self):
        self.assertFalse(factoring.is_prime(1))
        self.assertTrue(factoring.is_prime(29))
        self.assertEqual(factoring.primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(factoring.prime_factors(360), [2, 2, 2, 3, 3, 5])

    def test_random_numbers(self):
        first = factoring.random_numbers(42, 5)
        second = factoring.random_numbers(42, 5)
        self.assertEqual(first, second)
        for x in first:
            self.assertTrue(0 <= x < 1)

    def test_power_and_fibonacci(self):
        self.assertEqual(factoring.power(2, 100), 2 ** 100)
        self.assertEqual(factoring.power(5, 0), 1)
        self.assertEqual(factoring.nth_fibonacci(10), 55)
        self.assertEqual(factoring.nth_fibonacci(90), 2880067194370816120)
        with self.assertRaises(ValueError):
            factoring.power(2, -1)


if __name__ == "__main__":
    unittest.main()
