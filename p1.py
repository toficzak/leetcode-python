from typing import List


# time complexity:  O(n^2)
# space complexity: O(1)
def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# better approach - use hashMap to keep
# (desired value -> index of previously met number)
# then complexity should be O(n), but memory would rise to O(n), cause I would
# allocate at worst same array as input

# time complexity:  O(n)
# space complexity: O(n)
def two_sum(nums: List[int], target: int) -> List[int]:
    cache = {}
    for i, c in enumerate(nums):
        remaining = target - c
        if c in cache:
            return [cache[c], i]
        cache[remaining] = i
    return []

def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]


if __name__ == '__main__':
    examples = [
        [[2, 7, 11, 15], 9],
        [[3, 2, 4], 6],
        [[3, 3], 6]
    ]

    for example in examples:
        print(example)
        # result = two_sum_bruteforce(example[0], example[1])
        result = two_sum(example[0], example[1])
        print(result)
