from typing import List

def twoSum(nums: List[int], target: int) -> List[int] :
    for i in range(len(nums)) :
        num1 = nums[i]
        for j in range(len(nums)) :
            if i >= j : 
                pass
            else :
                num2 = nums[j]
                if num1 + num2 == target :
                    return [i, j]
