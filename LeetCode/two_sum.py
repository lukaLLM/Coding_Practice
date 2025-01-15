from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexed_map = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in indexed_map:
            return [indexed_map[difference], index]
        indexed_map[number] = index


twoSum([ 7, 11, 15,2], 9)