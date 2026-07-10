class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        curr = 0
        count = 0

        for num in nums:
            if num != curr:
                count = 1
                curr = num       
            else:
                count += 1
            if count > len(nums) // 2:
                return curr
        
        return curr

