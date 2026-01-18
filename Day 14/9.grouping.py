from itertools import groupby
data = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
    {"name": "spinach", "category": "vegetable"},
]


sorted_data = sorted(data, key=lambda x: x["category"])

for key, group in groupby(data, key=lambda x: x["category"]):
    print(key, list(group))
