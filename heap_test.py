import heapq
from heap import Heap


def is_min_heap_function_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.min_heap()

    heapq.heapify(keys)

    print(f"is min heap correct: {new_heap.min_heap() == keys}")
    new_heap.display_heap()

def is_max_heap_function_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap()


    heapq._heapify_max(keys)
    print(f"is max heap correct: {new_heap.max_heap() == keys}")
    new_heap.display_heap()


def is_peek_correct(keys: list):
    new_heap = Heap(keys)
    test_keys = keys
    
    heapq._heapify_max(test_keys)
    new_heap.max_heap() 

    print(f"is peek heap correct: {new_heap.peek()==heapq.nlargest(1,test_keys)[0]}")
    # new_heap.display_heap()

def is_pop_correct(keys: list):
    new_heap = Heap(keys)
    test_keys = keys
    
    max_heap = [-n for n in keys]
    heapq.heapify(max_heap)

    # Pop the maximum
    max_val = -heapq.heappop(max_heap)
    # print(test_keys)
    new_heap.max_heap()

    print(f"is pop correct: {(new_heap.pop() == max_val) and (test_keys == new_heap.max_heap())}")
    # new_heap.display_heap()

def is_neutralize_correct(keys: list):
    new_heap = Heap(keys)
    test_keys = keys
    
    max_heap = [-n for n in keys]
    heapq.heapify(max_heap)

    # Pop the maximum twice
    max_val = -heapq.heappop(max_heap)
    new_max = -heapq.heappop(max_heap)

    new_heap.max_heap()
    new_heap.neutralize()

    print(f"is neutralize correct: {test_keys == new_heap.max_heap()}")
    # new_heap.display_heap()

def is_left_child_corret(min_heap: list):
    return

def is_right_child_correct(min_heap: list):
    return

def is_parent_correct(min_heap: list):
    return

