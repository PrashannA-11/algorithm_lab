import unittest
from merge_sort import mergesort

class TestMergeSort(unittest.TestCase):

    def test_unsorted_list(self):
        self.assertEqual(mergesort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates(self):
        self.assertEqual(mergesort([4, 2, 4, 2, 4]), [2, 2, 4, 4, 4])

    def test_negative_numbers(self):
        self.assertEqual(mergesort([-3, -1, -4, -2]), [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(mergesort([3, -1, 4, -2, 0]), [-2, -1, 0, 3, 4])

if __name__ == '__main__':
    unittest.main()
