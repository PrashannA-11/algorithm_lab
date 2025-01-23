import unittest
from greedy_fracknapsack import fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):

    def test_knapsack_example_2(self):
        p = [80, 60, 50, 40]  # Profits
        w = [20, 10, 10, 10]  # Weights
        m = 30                # Maximum weight (capacity)

        total_profit, selected_items = fractional_knapsack(p, w, m)

        self.assertAlmostEqual(total_profit, 150, places=2)
        
        # Expected items based on value/weight ratio sorting
        expected_items = [
            (50, 10, 1.0),   
            (60, 10, 1.0),   
            (80, 20, 0.5)    # Partial item 
        ]
        
        selected_items_rounded = [(value, weight, round(fraction, 2)) for value, weight, fraction in selected_items]
        self.assertEqual(sorted(selected_items_rounded, key=lambda x: (x[0], x[1])), 
                         sorted(expected_items, key=lambda x: (x[0], x[1])))

    def test_knapsack_exact_capacity(self):
        p = [40, 30, 50]   # Profits
        w = [10, 20, 30]   # Weights
        m = 60             # Maximum weight (capacity)

        total_profit, selected_items = fractional_knapsack(p, w, m)

        self.assertAlmostEqual(total_profit, 120, places=2)
        
        expected_items = [
            (50, 30, 1.0),   
            (40, 10, 1.0),   
            (30, 20, 1.0)    
        ]
        
        selected_items_rounded = [(value, weight, round(fraction, 2)) for value, weight, fraction in selected_items]
        self.assertEqual(sorted(selected_items_rounded, key=lambda x: (x[0], x[1])), 
                         sorted(expected_items, key=lambda x: (x[0], x[1])))

    def test_knapsack_partial_selection(self):
        p = [100, 200, 150]  # Profits
        w = [10, 20, 40]     # Weights
        m = 30               # Maximum weight (capacity)

        total_profit, selected_items = fractional_knapsack(p, w, m)

        self.assertAlmostEqual(total_profit, 300, places=2)
        
        expected_items = [
            (100, 10, 1.0),    
            (200, 20, 1.0)
        ]
        
        selected_items_rounded = [(value, weight, round(fraction, 2)) for value, weight, fraction in selected_items]
        self.assertEqual(selected_items_rounded, expected_items)

if __name__ == '__main__':
    unittest.main()