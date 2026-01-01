import heapq
import unittest
from collections import defaultdict, Counter
from typing import List


# theoretical lower bound: O(n), cause each element must be inspected at least once, each can change result

# 1) frequency cache solution
# pattern: frequency counting with hash map
# create cache to keep frequencies, then sort resulting cache by values and return last k elements
# - time complexity: O(n) for cache creation, then sort O(logn) at worst case (all elements unique),
#   so O(n logn)
# - space complexity: O(n) - worst case, all elements in nums unique

# 2) bucket sort
# pattern: bucket/frequency counting
# Use a bounded integer range as array indices to avoid sorting.
# - time complexity: O(n) for dict creation, then O(n) for buckets creation and O(n) for retrieving result: O(n)
# - space complexity: O(n) - created dict

# 3) heap
# pattern: top k elements -> heap
# Use min-heap to keep k most frequent elements and compare next elements with the worst one.
# - time complexity: O(n) for aggregating frequencies,
#                    O(n) for iterating through each element, O(log k) for swapping elements and O(1) for ignoring,
#                    hence O(n log k)
# - space complexity: O(n) for frequencies array.
#                     O(k) for heap, so O(n) in general
class Solution:
    def topKFrequentSort(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_keys_by_freq = [k for k, _ in sorted(frequency.items(), key=lambda item: item[1], reverse=True)]
        return sorted_keys_by_freq[:k]

    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)  # initializes not existent keys with 0
        for num in nums:
            frequency[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in frequency.items():
            buckets[count].append(num)

        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result

        return []

    def topKFrequentIdiomatic(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        return [num for num, _ in frequency.most_common(k)]

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}  # map: number to frequency
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        heap = []  # by default, heapq keeps min-heap, that's what I need
        for number, frequency in frequencies.items():
            if len(heap) < k:
                heapq.heappush(heap, (frequency, number))
            else:
                if frequency > heap[0][0]:
                    heapq.heappushpop(heap, (frequency, number))

        return [number for _, number in heap]

    def topKFrequentHeapIdiomatic(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}  # map: number to frequency
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        topK = heapq.nlargest(k, frequencies.items(), key=lambda x: x[1])
        return [number for number, _ in topK]


class Test(unittest.TestCase):
    testcases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
        ([], 1, [])
    ]

    def testSort(self):
        for input_array, k, expected in self.testcases:
            with self.subTest(input_array):
                self.assertEqual(sorted(Solution().topKFrequentSort(input_array, k)), sorted(expected))

    def testBucketSort(self):
        for input_array, k, expected in self.testcases:
            with self.subTest(input_array):
                self.assertEqual(sorted(Solution().topKFrequentBucketSort(input_array, k)), sorted(expected))

    def testIdiomatic(self):
        for input_array, k, expected in self.testcases:
            with self.subTest(input_array):
                self.assertEqual(sorted(Solution().topKFrequentIdiomatic(input_array, k)), sorted(expected))

    def testHeap(self):
        for input_array, k, expected in self.testcases:
            with self.subTest(input_array):
                self.assertEqual(sorted(Solution().topKFrequentHeap(input_array, k)), sorted(expected))

    def testHeapIdiomatic(self):
        for input_array, k, expected in self.testcases:
            with self.subTest(input_array):
                self.assertEqual(sorted(Solution().topKFrequentHeapIdiomatic(input_array, k)), sorted(expected))
