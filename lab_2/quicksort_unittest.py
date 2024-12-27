import unittest
from quicksort import quicksort


class TestQuickSort(unittest.TestCase):


    def test_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5], 0, 4), [1, 2, 3, 4, 5])


    def test_unsorted_list(self):
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9, 2], 0, 6), [1, 1, 2, 3, 4, 5, 9])

    def test_duplicates(self):
        self.assertEqual(quicksort([4, 2, 4, 2, 4], 0, 4), [2, 2, 4, 4, 4])

    def test_mixed_numbers(self):
        self.assertEqual(quicksort([3, -1, 4, -2, 0], 0, 4), [-2, -1, 0, 3, 4])


if __name__ == '__main__':
    unittest.main()
