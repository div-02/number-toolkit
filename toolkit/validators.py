"""Input checking: keep asking until the user types a valid value."""


def get_int(prompt):
    """Ask for a whole number. Asks again if the input is not valid."""
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("  Please enter a whole number (like 12 or -5).")


def get_int_list(prompt):
    """Ask for numbers separated by spaces or commas and return a list."""
    while True:
        text = input(prompt)
        parts = text.replace(",", " ").split()
        numbers = []
        ok = len(parts) > 0
        for part in parts:
            try:
                numbers.append(int(part))
            except ValueError:
                ok = False
        if ok:
            return numbers
        print("  Please enter whole numbers separated by spaces (like 4 8 15).")
