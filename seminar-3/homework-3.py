
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

backpacks = []
for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
    backpacks.append(backpack)

full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)
print(result)

