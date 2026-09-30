"""Python collections (Unit 5): set operations and a dictionary of counts."""


def set_operations(list_a, list_b):
    """Union, intersection and differences of two lists, treated as sets."""
    a = set(list_a)
    b = set(list_b)
    result = {}
    result["union"] = sorted(a | b)
    result["intersection"] = sorted(a & b)
    result["only in A"] = sorted(a - b)
    result["only in B"] = sorted(b - a)
    return result


def frequency_table(arr):
    """Dictionary that maps each number to how many times it appears."""
    counts = {}
    for item in arr:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts
