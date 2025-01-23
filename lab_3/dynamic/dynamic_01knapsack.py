def knapsack_01_dp(values, weights, capacity):
    """
    Args:
    - values: List of values/profits for each item.
    - weights: List of weights for each item.
    - capacity: Maximum weight capacity of the knapsack.
    """
    n = len(values)
    
    # Initialize DP table with dimensions (n+1) x (capacity+1), all set to 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:  # If the item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # If the item cannot be included
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    max_value = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # If the item was included
            selected_items.append((i - 1, values[i - 1], weights[i - 1]))
            w -= weights[i - 1]
    
    selected_items.reverse()  # Reverse to maintain the original order
    return max_value, selected_items



