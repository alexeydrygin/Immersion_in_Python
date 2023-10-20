# lst = [1, 1, 2, 2, 3, 3]
lst = [1, 2, 3, 2, 4, 5, 4]

duplicates = set()
for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)
        
result = list(duplicates)
print(result)