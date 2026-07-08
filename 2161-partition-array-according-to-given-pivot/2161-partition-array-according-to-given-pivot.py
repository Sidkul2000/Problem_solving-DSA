class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # l, m, r = [], [], []
        # for n in nums:
        #     if n < pivot:
        #         l.append(n)
        #     elif n > pivot:
        #         r.append(n)
        #     else:
        #         m.append(n)
        # return l+m+r
        l, m = 0, 0
        r = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                nums[l] = nums[i]
                l += 1
            elif nums[i] > pivot:
                r.append(nums[i])
            else:
                m += 1
        return nums[:l] + [pivot]*m + r
