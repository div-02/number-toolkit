"""
Factoring methods (Unit 4): square root, smallest divisor, GCD, primes,
prime factors, pseudo-random numbers, big powers and the nth Fibonacci number.
"""


def square_root(n):
    """Square root using Newton's method (keep improving a guess)."""
    if n < 0:
        raise ValueError("cannot take the square root of a negative number")
    if n == 0:
        return 0.0
    guess = n / 2
    if n < 1:
        guess = 1.0
    for i in range(50):
        guess = (guess + n / guess) / 2
    return guess


def smallest_divisor(n):
    """Smallest divisor of n that is bigger than 1."""
    if n < 2:
        raise ValueError("number must be at least 2")
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i = i + 1
    return n


def gcd(a, b):
    """Greatest common divisor using Euclid's algorithm."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n):
    """True if n is a prime number."""
    if n < 2:
        return False
    return smallest_divisor(n) == n


def primes_up_to(limit):
    """List of all prime numbers from 2 up to limit."""
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def prime_factors(n):
    """List of prime factors of n, e.g. 12 gives [2, 2, 3]."""
    if n < 2:
        raise ValueError("number must be at least 2")
    factors = []
    while n > 1:
        d = smallest_divisor(n)
        factors.append(d)
        n = n // d
    return factors


def random_numbers(seed, count):
    """Pseudo-random numbers between 0 and 1 (linear congruential generator)."""
    numbers = []
    x = seed
    for i in range(count):
        x = (1103515245 * x + 12345) % (2 ** 31)
        numbers.append(x / (2 ** 31))
    return numbers


def power(base, exponent):
    """base ** exponent by repeated squaring (fast even for big exponents)."""
    if exponent < 0:
        raise ValueError("exponent must not be negative")
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base
        base = base * base
        exponent = exponent // 2
    return result


def nth_fibonacci(n):
    """The nth Fibonacci number (0th is 0, 1st is 1)."""
    if n < 0:
        raise ValueError("n must not be negative")
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
