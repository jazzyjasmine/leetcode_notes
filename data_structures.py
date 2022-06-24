import random
from typing import List
from collections import deque


class RandomizedSetSolution380:
    # 380. Insert Delete GetRandom O(1)
    # https://leetcode.com/problems/insert-delete-getrandom-o1/
    # Combination: list + hashmap
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


class UndergroundSystemSolution1396:
    # 1396. Design Underground System
    # Non-combination: hashmap
    # https://leetcode.com/problems/design-underground-system/

    def __init__(self):
        self.checkedin = {}
        self.durations = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedin[id] = [stationName, t]

        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedin.pop(id)
        duration = t - startTime
        if (startStation, stationName) not in self.durations:
            self.durations[(startStation, stationName)] = [duration]
        else:
            self.durations[(startStation, stationName)].append(duration)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        duration_list = self.durations[(startStation, endStation)]
        return sum(duration_list) / len(duration_list)


class WordDistanceSolution244:
    # 244. Shortest Word Distance II
    # Time: O(n), Space: O(n)
    # shortest: Find min diff between two sorted lists is O(max(k, l)),
    # where k and l are the number of occurences of two words. k = O(n),
    # l = O(n), therefore time is O(n). No need O(n^2).
    # reference: https://leetcode.com/problems/shortest-word-distance-ii/solution/
    # https://leetcode.com/problems/shortest-word-distance-ii/

    def __init__(self, wordsDict: List[str]):
        self.word_to_index = {word: [] for word in wordsDict}
        for index, word in enumerate(wordsDict):
            self.word_to_index[word].append(index)
               

    def shortest(self, word1: str, word2: str) -> int:
        ptr1, ptr2 = 0, 0
        word1_indexes = self.word_to_index[word1]
        word2_indexes = self.word_to_index[word2]
        shortest_distance = float('inf')
        
        while ptr1 < len(word1_indexes) and ptr2 < len(word2_indexes):
            shortest_distance = min(shortest_distance, abs(word1_indexes[ptr1] - word2_indexes[ptr2]))
            if word1_indexes[ptr1] > word2_indexes[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
        
        return shortest_distance
            
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


class MovingAverage346:
    # 346. Moving Average from Data Stream
    # https://leetcode.com/problems/moving-average-from-data-stream/

    def __init__(self, size: int):
        self.count = 0
        self.size = size
        self.queue = deque([])

    def next(self, val: int) -> float:
        if self.count == self.size:
            self.queue.popleft()
            self.queue.append(val)
        else:
            self.queue.append(val)
            self.count += 1
        return sum(self.queue) / self.count
        