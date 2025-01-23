import unittest
from brute_01knapsack import brute_01knapsack

class TestBrute01Knapsack(unittest.TestCase):

    def test_knapsack_example_1(self):
        # Test case 1: Test with different weights and profits
        p = [80, 60, 50, 40]  # Profits
        w = [20, 10, 10, 10]  # Weights
        m = 30                # Maximum weight (capacity)

        # Updated expected solution and profit
        expected_solution = '0111'  # Binary representation of selected items
        expected_profit = 150       # Profit from the selected items
        
        solution, max_profit = brute_01knapsack(p, w, m)
        self.assertEqual(solution, expected_solution)
        self.assertEqual(max_profit, expected_profit)

    def test_knapsack_large_capacity(self):
        # Test case 2: Test where all items can fit within the capacity
        p = [10, 20, 30, 40]  # Profits
        w = [1, 2, 3, 4]      # Weights
        m = 10                # Maximum weight (capacity)
        
        # All items can be selected
        expected_solution = '1111'  # Binary representation of all items selected
        expected_profit = 100       # Profit from all selected items
        
        solution, max_profit = brute_01knapsack(p, w, m)
        self.assertEqual(solution, expected_solution)
        self.assertEqual(max_profit, expected_profit)

    def test_knapsack_over_capacity(self):
        # Test case 3: Test with a set of items where none can be selected due to capacity
        p = [10, 20, 30]  # Profits
        w = [10, 20, 30]  # Weights
        m = 5             # Maximum weight (capacity)

        # None of the items can be selected because all are heavier than the capacity
        expected_solution = '000'  # No items selected
        expected_profit = 0        # No profit
        
        solution, max_profit = brute_01knapsack(p, w, m)
        self.assertEqual(solution, expected_solution)
        self.assertEqual(max_profit, expected_profit)

if __name__ == '__main__':
    unittest.main()
