"""
Number Toolkit - run with:  python main.py

A menu-driven program that runs the algorithms from the Python Essentials course.
"""

from toolkit import fundamentals, factoring, arrays, collections_ops
from toolkit.validators import get_int, get_int_list
from toolkit.logger import log


def show_result(name, result):
    '''Print a result and save it in the log file.'''
    print("  Result:", result)
    log(name + " -> " + str(result))


def fundamentals_menu():
    while True:
        print("\n--- Fundamental Algorithms ---")
        print("1. Swap two values")
        print("2. Count digits of a number")
        print("3. Sum of a list of numbers")
        print("4. Factorial")
        print("5. Fibonacci sequence")
        print("6. Reverse a number")
        print("7. Convert to another base (2-16)")
        print("8. Convert a digit string to a number")
        print("0. Back to main menu")
        choice = input("Choose: ").strip()
        try:
            if choice == "0":
                return
            elif choice == "1":
                a = input("  First value: ")
                b = input("  Second value: ")
                show_result("swap", fundamentals.swap(a, b))
            elif choice == "2":
                n = get_int("  Number: ")
                show_result("count digits of " + str(n), fundamentals.count_digits(n))
            elif choice == "3":
                numbers = get_int_list("  Numbers (separated by spaces): ")
                show_result("sum", fundamentals.summation(numbers))
            elif choice == "4":
                n = get_int("  Number: ")
                show_result("factorial " + str(n), fundamentals.factorial(n))
            elif choice == "5":
                count = get_int("  How many Fibonacci numbers? ")
                show_result("fibonacci list", fundamentals.fibonacci_list(count))
            elif choice == "6":
                n = get_int("  Number: ")
                show_result("reverse " + str(n), fundamentals.reverse_number(n))
            elif choice == "7":
                n = get_int("  Number (0 or more): ")
                base = get_int("  Base (2-16): ")
                show_result("base conversion", fundamentals.convert_base(n, base))
            elif choice == "8":
                text = input("  Digit string: ")
                show_result("string to number", fundamentals.string_to_number(text))
            else:
                print("  Invalid choice, please pick a number from the menu.")
        except ValueError as error:
            print("  Error:", error)
            log("error in fundamentals menu: " + str(error))


def factoring_menu():
    while True:
        print("\n--- Factoring Methods ---")
        print("1. Square root")
        print("2. Smallest divisor")
        print("3. GCD of two numbers")
        print("4. Prime numbers up to n")
        print("5. Prime factors")
        print("6. Pseudo-random numbers")
        print("7. Raise a number to a power")
        print("8. nth Fibonacci number")
        print("0. Back to main menu")
        choice = input("Choose: ").strip()
        try:
            if choice == "0":
                return
            elif choice == "1":
                n = get_int("  Number: ")
                show_result("square root of " + str(n), round(factoring.square_root(n), 6))
            elif choice == "2":
                n = get_int("  Number (2 or more): ")
                show_result("smallest divisor of " + str(n), factoring.smallest_divisor(n))
            elif choice == "3":
                a = get_int("  First number: ")
                b = get_int("  Second number: ")
                show_result("gcd", factoring.gcd(a, b))
            elif choice == "4":
                n = get_int("  Up to: ")
                show_result("primes up to " + str(n), factoring.primes_up_to(n))
            elif choice == "5":
                n = get_int("  Number (2 or more): ")
                show_result("prime factors of " + str(n), factoring.prime_factors(n))
            elif choice == "6":
                seed = get_int("  Seed (any whole number): ")
                count = get_int("  How many numbers? ")
                numbers = factoring.random_numbers(seed, count)
                rounded = []
                for x in numbers:
                    rounded.append(round(x, 4))
                show_result("random numbers", rounded)
            elif choice == "7":
                base = get_int("  Base: ")
                exponent = get_int("  Exponent (0 or more): ")
                show_result("power", factoring.power(base, exponent))
            elif choice == "8":
                n = get_int("  n: ")
                show_result("fibonacci number " + str(n), factoring.nth_fibonacci(n))
            else:
                print("  Invalid choice, please pick a number from the menu.")
        except ValueError as error:
            print("  Error:", error)
            log("error in factoring menu: " + str(error))


def arrays_menu():
    while True:
        print("\n--- Arrays and Collections ---")
        print("1. Reverse a list")
        print("2. Count how many times a number appears")
        print("3. Largest number in a list")
        print("4. Remove duplicates from a SORTED list")
        print("5. Partition a list around a pivot")
        print("6. k-th smallest number")
        print("7. Set operations on two lists")
        print("8. Frequency table (dictionary)")
        print("0. Back to main menu")
        choice = input("Choose: ").strip()
        try:
            if choice == "0":
                return
            elif choice == "1":
                arr = get_int_list("  List: ")
                show_result("reverse", arrays.reverse_array(arr))
            elif choice == "2":
                arr = get_int_list("  List: ")
                target = get_int("  Number to count: ")
                show_result("count", arrays.count_occurrences(arr, target))
            elif choice == "3":
                arr = get_int_list("  List: ")
                show_result("maximum", arrays.find_max(arr))
            elif choice == "4":
                arr = get_int_list("  Sorted list: ")
                show_result("remove duplicates", arrays.remove_duplicates_sorted(arr))
            elif choice == "5":
                arr = get_int_list("  List: ")
                pivot = get_int("  Pivot: ")
                smaller, equal, larger = arrays.partition_array(arr, pivot)
                show_result("partition", "smaller=" + str(smaller) + " equal=" + str(equal) + " larger=" + str(larger))
            elif choice == "6":
                arr = get_int_list("  List: ")
                k = get_int("  k (1 = smallest): ")
                show_result("k-th smallest", arrays.kth_smallest(arr, k))
            elif choice == "7":
                list_a = get_int_list("  First list: ")
                list_b = get_int_list("  Second list: ")
                results = collections_ops.set_operations(list_a, list_b)
                for name in results:
                    print("  " + name + ":", results[name])
                log("set operations")
            elif choice == "8":
                arr = get_int_list("  List: ")
                show_result("frequency table", collections_ops.frequency_table(arr))
            else:
                print("  Invalid choice, please pick a number from the menu.")
        except ValueError as error:
            print("  Error:", error)
            log("error in arrays menu: " + str(error))


def main():
    print("=== Number Toolkit ===")
    log("program started")
    while True:
        print("\n--- Main Menu ---")
        print("1. Fundamental algorithms")
        print("2. Factoring methods")
        print("3. Arrays and collections")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            fundamentals_menu()
        elif choice == "2":
            factoring_menu()
        elif choice == "3":
            arrays_menu()
        elif choice == "0":
            print("Goodbye!")
            log("program ended")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 0.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
