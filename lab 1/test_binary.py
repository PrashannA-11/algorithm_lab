import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    
    def test_element_present(self):
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 30), 2)
    
    def test_element_not_present(self):
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 60), -1)

if __name__ == '__main__':
    unittest.main()