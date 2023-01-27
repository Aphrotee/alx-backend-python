import utils
access_nested_map = __import__('utils').access_nested_map


n = {'a': 'p', 'b': {'a': 3, 'b':[1,2,3]}}
print(access_nested_map(n, ('b', 'a')))