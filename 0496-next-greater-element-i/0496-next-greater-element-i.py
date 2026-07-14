class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []
        res = []
        for i in nums2:
            while stack and stack[-1] <= i:
                ele = stack.pop()
                mp[ele] = i
            stack.append(i)
        for i in nums1:
            if i not in mp:
                res.append(-1)
            else:
                res.append(mp[i])
        return res
