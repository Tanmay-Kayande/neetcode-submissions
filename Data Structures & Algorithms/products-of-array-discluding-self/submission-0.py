class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []
        product = 1
        for i in range(len(nums)):
            
            if i == 0:
                prefix.append(1)
            else:
                product *= nums[i-1]
                prefix.append(product)
        product = 1
        for i in range(len(nums)-1,-1,-1):
            
            if i == len(nums)-1:
                suffix.append(1)
            else:
                product *= nums[i+1]
                suffix.append(product)
        suffix.reverse()
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        return res