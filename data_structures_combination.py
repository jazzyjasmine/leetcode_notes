import random


class RandomizedSetSolution380:
    # 380. Insert Delete GetRandom O(1)
    # https://leetcode.com/problems/insert-delete-getrandom-o1/
    # list + hashmap
    # list: insert O(1), getRandom O(1), delete O(n) because iterate through the list
    # hashset: insert O(1), getRandom N/A because no index, delete O(1)

    # solution for delete O(n) of list: use hashmap to store the index for each element

    def __init__(self):
        self.list = []  # use list to store elements, instead of set
        self.num_to_index = dict()

        
    def insert(self, val: int) -> bool:
        if val not in self.num_to_index:
            self.list.append(val)
            self.num_to_index[val] = len(self.list) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.num_to_index:
            curr_index = self.num_to_index[val]
            last_index_value = self.list[-1]
            self.list[curr_index] = last_index_value
            self.list.pop()
            self.num_to_index[last_index_value] = curr_index
            del self.num_to_index[val]  # this line can not change order with the previous line, e.g. self.list = [0]
            return True
        return False
            

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.list) - 1)
        return self.list[random_index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
