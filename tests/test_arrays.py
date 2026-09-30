import unittest

from toolkit import arrays, collections_ops


class TestArrays(unittest.TestCase):
    def test_reverse_count_max(self):
        self.assertEqual(arrays.reverse_array([1, 2, 3]), [3, 2, 1])
        self.assertEqual(arrays.count_occurrences([1, 2, 2, 3], 2), 2)
        self.assertEqual(arrays.find_max([3, 9, 2]), 9)
        with self.assertRaises(ValueError):
            arrays.find_max([])

    def test_remove_duplicates(self):
        self.assertEqual(arrays.remove_duplicates_sorted([1, 1, 2, 3, 3]), [1, 2, 3])
        with self.assertRaises(ValueError):
            arrays.remove_duplicates_sorted([3, 1])

    def test_partition_and_kth(self):
        self.assertEqual(arrays.partition_array([5, 1, 5, 9], 5), ([1], [5, 5], [9]))
        self.assertEqual(arrays.kth_smallest([7, 10, 4, 3, 20, 15], 3), 7)
        with self.assertRaises(ValueError):
            arrays.kth_smallest([1, 2], 5)


class TestCollections(unittest.TestCase):
    def test_sets(self):
        result = collections_ops.set_operations([1, 2, 3], [2, 3, 4])
        self.assertEqual(result["union"], [1, 2, 3, 4])
        self.assertEqual(result["intersection"], [2, 3])
        self.assertEqual(result["only in A"], [1])

    def test_frequency(self):
        self.assertEqual(collections_ops.frequency_table([1, 1, 2]), {1: 2, 2: 1})


if __name__ == "__main__":
    unittest.main()
