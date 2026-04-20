class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for j in range(1, n):
            i = 0
            k = n-1
            while i<j and j< k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    k -=1
        return ans       