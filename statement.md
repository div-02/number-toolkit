# Problem Statement

## Problem
When learning programming, it is easy to use built-in functions like `math.gcd` or `sorted()` without understanding how they work. There is no single small tool where the main algorithms from the Python Essentials course can be run, tested and read in one place.

## Scope
A menu-driven command-line program written in Python (standard library only). Every algorithm is written by hand instead of using built-in shortcuts. Out of scope: graphical interface, database, internet access.

## Target Users
- First-year students who want to revise algorithms
- Teachers who want simple runnable example code for demonstration

## High-Level Features
1. **Fundamental algorithms:** swap, count digits, sum, factorial, Fibonacci, reverse a number, base conversion, string to number
2. **Factoring methods:** square root, smallest divisor, GCD, primes, prime factors, pseudo-random numbers, big powers, nth Fibonacci number
3. **Arrays and collections:** reverse, count, maximum, remove duplicates from a sorted list, partition, k-th smallest, set operations, frequency dictionary
4. Numbered menus with input checking (the program asks again if the input is wrong)
5. A log file (`toolkit.log`) and unit tests

## Non-Functional Requirements
1. **Usability:** simple numbered menus and clear messages
2. **Reliability:** wrong input never crashes the program; it shows a message and continues
3. **Maintainability:** one file per topic, input checking kept separate, tests for each module
4. **Performance:** repeated squaring for powers (O(log n)), Euclid's method for GCD, square-root limit for divisors
5. **Logging:** results and errors are saved with a time in `toolkit.log`
6. **Portability:** Python 3.8 or newer, no extra packages, works on Windows, macOS and Linux
