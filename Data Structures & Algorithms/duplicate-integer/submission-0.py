class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=len(set(nums))
        n=len(nums)
        if(s==n):
            return False
        return True