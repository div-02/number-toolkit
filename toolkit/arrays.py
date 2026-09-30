"""
Array techniques (Unit 5): reverse, count, maximum, remove duplicates,
partition and the k-th smallest element.
"""


def reverse_array(arr):
    """Return a new list with the items in reverse order."""
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result


def count_occurrences(arr, target):
    """How many times target appears in the list."""
    count = 0
    for item in arr:
        if item == target:
            count = count + 1
    return count


def find_max(arr):
    """Largest number in the list."""
    if len(arr) == 0:
        raise ValueError("the list is empty")
    biggest = arr[0]
    for item in arr:
        if item > biggest:
            biggest = item
    return biggest


def remove_duplicates_sorted(arr):
    """Remove duplicates from a list that is already sorted (smallest first)."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            raise ValueError("the list must be sorted from smallest to largest")
    result = []
    for item in arr:
        if len(result) == 0 or result[-1] != item:
            result.append(item)
    return result


def partition_array(arr, pivot):
    """Split a list into three lists: smaller, equal and larger than pivot."""
    smaller = []
    equal = []
    larger = []
    for item in arr:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            larger.append(item)
    return smaller, equal, larger


def kth_smallest(arr, k):
    """The k-th smallest number (k = 1 means the smallest)."""
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the list")
    items = list(arr)
    # selection sort: move the smallest remaining item to the front each time
    for i in range(len(items)):
        smallest_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
        items[i], items[smallest_index] = items[smallest_index], items[i]
    return items[k - 1]
