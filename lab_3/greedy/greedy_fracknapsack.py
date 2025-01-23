def fractional_knapsack(p, w, m):
    # Combine profits and weights into a list of tuples (value, weight, ratio)
    n = len(p)
    items = [(p[i], w[i], p[i] / w[i]) for i in range(n)]
    
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_profit = 0
    capacity_left = m
    selected_items = []  # To keep track of selected items and their fractions
    
    for value, weight, ratio in items:
        if capacity_left == 0:  # If the knapsack is full, stop
            break
        
        if weight <= capacity_left:  # Take the entire item
            total_profit += value
            capacity_left -= weight
            selected_items.append((value, weight, 1.0))  # Full item taken
        else:  # Take a fraction of the item
            fraction = capacity_left / weight
            total_profit += value * fraction
            selected_items.append((value, weight, fraction))
            capacity_left = 0  # Knapsack is now full
    
    return total_profit, selected_items


