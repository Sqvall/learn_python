from itertools import permutations, combinations, combinations_with_replacement

string = 'ABC'
elements = 2

print(list(permutations(string, elements)))
print(list(combinations(string, elements)))
print(list(combinations_with_replacement(string, elements)))
