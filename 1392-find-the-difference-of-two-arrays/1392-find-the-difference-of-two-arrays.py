class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        answer1 = set()
        answer2 = set()
        for i in range(n1):
            if nums1[i] not in nums2:
                answer1.add(nums1[i])
        for j in range(n2):
            if nums2[j] not in nums1:
                answer2.add(nums2[j])
        answer = [list(answer1), list(answer2)]
        return answer

        
        