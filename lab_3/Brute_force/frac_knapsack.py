from itertools import product

def brute_force_fractional_knapsack(profits, weights, capacity, step=0.01):
    n = len(profits)
    max_profit = 0
    best_combo = [0] * n

    fractions = [[i*step for i in range(int(1/step)+1)] for _ in range(n)]
    for combo in product(*fractions):
        weight = sum(w*f for w,f in zip(weights,combo))
        if weight <= capacity:
            profit = sum(p*f for p,f in zip(profits,combo))
            if profit > max_profit:
                max_profit = profit
                best_combo = list(combo)
    
    return max_profit, best_combo