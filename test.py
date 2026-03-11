from heap_test import is_min_heap_function_correct,is_max_heap_function_correct,is_peek_correct, is_pop_correct, is_neutralize_correct
from hashing import Hashing

items = [2, 5, 3, 0, 1, 0, 4, 6]
items = [4,1,3,2,16,9,10,14,8,7]

is_min_heap_function_correct(items)
print('\n')
is_max_heap_function_correct(items)
print('\n')
is_peek_correct(items)
print('\n')
is_pop_correct(items)
print('\n')
is_neutralize_correct(items)
print('\n')
newHash = Hashing(items)
newHash.hash_keys()