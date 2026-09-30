"""
Fundamental algorithms (Unit 3): swap, counting, summation, factorial,
Fibonacci, reverse, base conversion and character-to-number conversion.
"""


def swap(a, b):
    """Exchange two values using tuple assignment."""
    a, b = b, a
    return a, b


def count_digits(n):
    """Count how many digits a whole number has."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count


def summation(numbers):
    """Add up all the numbers in a list."""
    total = 0
    for x in numbers:
        total = total + x
    return total


def factorial(n):
    """Return n! (n must not be negative)."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def fibonacci_list(count):
    """Return the first `count` Fibonacci numbers as a list."""
    numbers = []
    a = 0
    b = 1
    for i in range(count):
        numbers.append(a)
        a, b = b, a + b
    return numbers


def reverse_number(n):
    """Reverse the digits of a number, e.g. 1234 becomes 4321."""
    negative = n < 0
    n = abs(n)
    reversed_n = 0
    while n > 0:
        last_digit = n % 10
        reversed_n = reversed_n * 10 + last_digit
        n = n // 10
    if negative:
        reversed_n = -reversed_n
    return reversed_n


def convert_base(n, base):
    """Convert a whole number (0 or more) to a base between 2 and 16."""
    if n < 0:
        raise ValueError("number must not be negative")
    if base < 2 or base > 16:
        raise ValueError("base must be between 2 and 16")
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    return result


def string_to_number(text):
    """Turn a string of digits into a number without using int()."""
    text = text.strip()
    negative = False
    if text.startswith("-"):
        negative = True
        text = text[1:]
    if text == "":
        raise ValueError("please enter some digits")
    value = 0
    for ch in text:
        if ch < "0" or ch > "9":
            raise ValueError("only the digits 0-9 are allowed")
        value = value * 10 + (ord(ch) - ord("0"))
    if negative:
        value = -value
    return value
