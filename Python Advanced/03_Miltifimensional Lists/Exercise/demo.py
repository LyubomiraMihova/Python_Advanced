import itertools

l = [[1,2], [4,5], [9,10]]

print(list(itertools.chain(*l)))