data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(n):
    total = 0
    if type(n) == int or type(n) == float:
        total += n
    elif type(n) == str:
        total += len(n)
    elif type(n) in [list, tuple, set]:
        for elem in n:
            total += calculate_structure_sum(elem)
    elif type(n) == dict:
        for k,v in n.items():
            total += calculate_structure_sum(k)
            total += calculate_structure_sum(v)
    return total

result = calculate_structure_sum(data_structure)
print(result)