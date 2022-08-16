group1 = [10, 9, 10, 7, 8, 4, 5, 7, 10]
group2 = [9, 7, 6, 6, 5, 7, 6, 7, 8, 7]
group3 = [3, 4, 10, 10, 10, 9, 9, 4, 4]

print(*(set(group1) & set(group2) & set(group3)))
print(*(set(range(1, 11)) - set(group1 + group2 + group3)))
