import unittest
from dynamic_01knapsack import knapsack_01_dp

class TestKnapsack01DP(unittest.TestCase):

    def test_case_1(self):  # all items have the same weight
        values = [10, 20, 30]
        weights = [1, 1, 1]
        capacity = 2
        expected_max_value = 50
        expected_selected_items = [(1, 20, 1), (2, 30, 1)]
        
        max_value, selected_items = knapsack_01_dp(values, weights, capacity)
        
        if max_value != expected_max_value or selected_items != expected_selected_items:
            print(f"Test Case 1 Failed:")
            print(f"Expected: {expected_max_value}, {expected_selected_items}")
            print(f"Got: {max_value}, {selected_items}")
        
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)

    def test_case_2(self):  # more complex case with varied weight and values
        values = [20, 5, 10, 40, 15, 25]
        weights = [1, 2, 3, 8, 7, 4]
        capacity = 10
        expected_max_value = 60
        expected_selected_items = [(0, 20, 1), (3, 40, 8)]  # Updated selected items

        
        max_value, selected_items = knapsack_01_dp(values, weights, capacity)
        
        if max_value != expected_max_value or selected_items != expected_selected_items:
            print(f"Test Case 2 Failed:")
            print(f"Expected: {expected_max_value}, {expected_selected_items}")
            print(f"Got: {max_value}, {selected_items}")
        
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)

if __name__ == "__main__":
    unittest.main()
