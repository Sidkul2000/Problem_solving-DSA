class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # n = len(arr)
        # s = 1
        # arr.sort()
        # print(arr)
        # ans = {}
        # if n == 1:
        #     return True
        # for i in range(n-1):
        #     if arr[i+1] == arr[i]:
        #         s += 1
        #     else:
        #         ans[arr[i]] = s
        #         s = 1
        # ans[arr[n-1]] = s
        # if len(set(ans.values())) == len(ans):
        #     return True
        # else:
        #     return False
        c = Counter(arr).values()
        return len(c)==len(set(c))