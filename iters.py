from itertools import permutations

for _ in permutations('ABC'):
    print("".join(_))

print(type(permutations('ABC')))