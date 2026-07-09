class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    final_list += [i]
                    final_list += [j]
                    return final_list