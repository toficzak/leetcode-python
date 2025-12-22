from typing import List


def specialTriplets(nums: List[int]) -> int:
    # frequency map: int -> freq
    freq_after = {}
    freq_before = {}
    result = 0

    for index in range(0, len(nums)):
        if nums[index] not in freq_after:
            freq_after[nums[index]] = 0
        freq_after[nums[index]] += 1

    for index in range(0, len(nums)):
        freq_after[nums[index]] -= 1
        key = 2 * nums[index]
        count_before = freq_before.get(key, 0)
        count_after = freq_after.get(key, 0)
        result += count_before * count_after

        if nums[index] not in freq_before:
            freq_before[nums[index]] = 0
        freq_before[nums[index]] += 1
    return result % (10 ** 9 + 7)


if __name__ == '__main__':
    print(specialTriplets([6, 3, 6]))
    print(specialTriplets([0, 1, 0, 0]))
    print(specialTriplets([8, 4, 2, 8, 4]))
