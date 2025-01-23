import unittest
from frac_knapsack import brute_force_fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):


    def test_multiple_items(self):
        profits = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        max_profit, solution = brute_force_fractional_knapsack(profits, weights, capacity)
        self.assertAlmostEqual(max_profit, 240.0, delta=0.01)
        self.assertAlmostEqual(solution, [1.0, 1.0, 0.67], delta=0.01)

    def test_capacity_exceeded(self):
        profits = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 40
        max_profit, solution = brute_force_fractional_knapsack(profits, weights, capacity)
        self.assertAlmostEqual(max_profit, 220.0, delta=0.01)
        self.assertAlmostEqual(solution, [1.0, 1.0, 0.33], delta=0.01)

if __name__ == '__main__':
    unittest.main()