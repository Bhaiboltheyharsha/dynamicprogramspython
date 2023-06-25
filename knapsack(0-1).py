def knapsack(items, capacity):
    bag = []
    items = sorted(items, key=lambda x:x['value'], reverse=True )
    for item in items:
        if item['weight'] <= capacity:
            bag.append(item)
            capacity -= item['weight']

    total_value = 0
    for item in bag:
        total_value += item['value']
    return bag, total_value

items = [
    {"value": 10, "weight": 7},
    {"value": 20, "weight": 4},
    {"value": 12, "weight": 5},
    {"value": 32, "weight": 2},
    {"value": 34, "weight": 7},
]
cap = 15
ans = knapsack(items, cap)
print(ans)