class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = []

        for i in range(len(nums)):
            if nums[i] not in temp_list:
                temp_list += [nums[i]]
            else:
                return True
        return False