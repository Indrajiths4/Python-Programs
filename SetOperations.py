# Set operations: Union, Intersection, Difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference (elements in set1 but not in set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Check if one set is a subset of another
subset1 = {1, 2}
subset2 = {1, 2, 3}

print("Is subset1 a subset of set1?", subset1.issubset(set1))
print("Is subset2 a subset of set1?", subset2.issubset(subset1))
