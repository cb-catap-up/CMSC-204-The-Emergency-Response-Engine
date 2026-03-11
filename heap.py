import math

class Heap:
    def __init__(self, keys):
        self.keys = keys
        self.heap = []
    def display_heap(self):
        """
        Display heap (works for heaps up to 4 levels)
        """

        if not self.heap:
            print("Heap is empty")
            return
        nodes = self.get_current_nodes_for_each_level()
        number_of_node_statements = len(nodes)
        node_number_iterator = 1
        next_node_index_to_print = 0

        separator_for_1_first_level = "/   \\"
        separator_for_1_second_level = "/     \\"
        separator_for_1_third_level = "/       \\"
        separator_for_1_fourth_level = "/         \\"

        second_single_spacer_unit = "/   "
        second_spacer_unit = "/   \\"

        count_third_layer = len(nodes[2])
        if count_third_layer == 2:
            second_spacer_unit_two = ""
        elif count_third_layer == 3:
            second_spacer_unit_two = f"{second_single_spacer_unit}"
        else:
            second_spacer_unit_two = second_spacer_unit

        # build separator dynamically
        separator_for_second_level = f"{second_spacer_unit}{' ' * 7}{second_spacer_unit_two}"

        separator_for_third_level = '/ \\'
        if number_of_node_statements == 4:
            third_spacer_single_unit = "/ "
            third_spacer_unit = "/ \\"

            count = len(nodes[3])

            groups = count // 2

            spacers = [third_spacer_unit] * groups

            # if odd number of nodes, add single branch pieces
            if count % 2 == 1:
                spacers.append(third_spacer_single_unit)

            separator_for_third_level = (" " * 3).join(spacers)

        second_level_spacer = 11 * " "
        third_level_spacer = 5 * " "
        fourth_level_spacer = 3 * " "
        inbetween_spacer = " "

        for i in range(number_of_node_statements):

            item_to_print = ""

            spacer = third_level_spacer
            
            item_counter = 1

            for _ in range(node_number_iterator):
                if next_node_index_to_print >= len(self.heap):
                    break

                if item_counter % 2 == 0:
                    spacer = inbetween_spacer
                    if i == 2:
                        spacer = inbetween_spacer *5
                else:
                    if i == 1:
                        spacer = second_level_spacer
                    elif i == 2:
                        spacer = third_level_spacer
                    elif i == 3:
                        spacer = fourth_level_spacer

                item_to_print += str(self.heap[next_node_index_to_print]) + spacer
                next_node_index_to_print += 1
                item_counter += 1

            if i == 0:
                print(f"{12*' '}{item_to_print}")
                print(f"{10*' '}{separator_for_1_first_level}")
                print(f"{9*' '}{separator_for_1_second_level}")
                print(f"{8*' '}{separator_for_1_third_level}")
                print(f"{7*' '}{separator_for_1_fourth_level}")
            elif i == 1:
                print(f"{6*' '}{item_to_print}")
                print(f"{4*' '}{separator_for_second_level}")
            elif i == 2:
                print(f"{3*' '}{item_to_print}")
                if number_of_node_statements == 4:
                    print(f"{2*' '}{separator_for_third_level}")
            else:
                print(f"{1*' '}{item_to_print}")

            node_number_iterator *= 2
        
    def _get_parent_index(self, index):
        return len(index)//2

    def _get_left_children_index(self, index):
        return 2*index + 1

    def _get_right_children_index(self, index):
        return 2*index + 2

    def _heapify_min(self,keys: list, index):
        while True:
            parent = index
            left_item = self._get_left_children_index(index)
            right_item = self._get_right_children_index(index)

            if left_item < len(keys) and keys[left_item] < keys[parent]:
                parent = left_item
            if right_item < len(keys) and keys[right_item] < keys[parent]:
                parent = right_item
            if parent == index:
                break
            keys[index], keys[parent] = keys[parent], keys[index]
            index = parent
        return keys
    
    def _heapify_max(self,keys: list, index):
        while True:
            parent = index
            left_item = self._get_left_children_index(index)
            right_item = self._get_right_children_index(index)

            if left_item < len(keys) and keys[left_item] > keys[parent]:
                parent = left_item
            if right_item < len(keys) and keys[right_item] > keys[parent]:
                parent = right_item
            if parent == index:
                break
            keys[index], keys[parent] = keys[parent], keys[index]
            index = parent
        return keys

    def min_heap(self):
        self.heap = self.keys.copy()

        for i in range(len(self.heap)//2):
            self._heapify_min(self.heap, i)
        return self.heap
    
    def max_heap(self):
        self.heap = self.keys.copy()
        for i in range(len(self.heap)//2):
            self.heap = self._heapify_max(self.keys,i)
        return self.heap

    def peek(self):
        return self.keys[0]

    def bubble_down(self, index):
        n = len(self.keys)

        while True:
            largest = index
            left = self._get_left_children_index(index)
            right = self._get_right_children_index(index)

            if left < n and self.keys[left] > self.keys[largest]:
                largest = left
            if right < n and self.keys[right] > self.keys[largest]:
                largest = right

            if largest == index:
                break

            # show what is bubbling
            print(f"{self.keys[index]} moved down, {self.keys[largest]} moved up")

            # swap
            self.keys[index], self.keys[largest] = self.keys[largest], self.keys[index]

            index = largest

            # show heap after each swap
            self.display_heap()
            print('\n')
    
    def get_current_nodes_for_each_level(self):
        if not self.heap:
            raise IndexError("no items from heap")

        height = math.floor(math.log2(len(self.heap)))

        levels = []

        for level in range(height + 1):
            start = 2**level - 1
            end = min(2**(level + 1) - 2, len(self.heap) - 1)

            current_level = self.heap[start:end+1]
            levels.append(current_level)

        return levels


    def pop(self):
        if not self.keys:
            raise IndexError("pop from empty heap")
        # show initial
        self.display_heap()
        # Swap root with last element, then remove last element so it can bubble down
        last_index = len(self.keys) - 1
        self.keys[0], self.keys[last_index] = self.keys[last_index], self.keys[0]
        item = self.keys.pop()  # Remove the max (old root)

        print("swap first and last index and remove the last")
        # show heap after each swap
        self.display_heap()
        print('\n')
        # # Bubble down the new root to restore heap property
        if self.keys:
            self.bubble_down(0)

        return item

    # remove the two larges values
    def neutralize(self):
        for _ in range(2):
            self.pop()