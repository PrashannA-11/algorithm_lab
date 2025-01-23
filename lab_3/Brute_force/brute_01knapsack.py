def get_String(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def brute_01knapsack(p,w,m):
    assert len(p) == len(w)

    n = len(p)
    bit_strings = get_String(n)

    max_profit = 0
    solution = ''

    for s in bit_strings:
        weight = sum([int(s[i])*w[i] for i in range(n)])
        if weight > m:
            continue
        profit = sum([int(s[i])*p[i] for i in range(n)])
        max_profit = max(max_profit, profit)
        if max_profit == profit:
            solution = s
    return solution, max_profit
