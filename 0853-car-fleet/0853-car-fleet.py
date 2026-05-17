class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {}
        stack=[]
        for i in range(len(speed)):
            mp[position[i]] = speed[i]
        sorted_mp = sorted(mp, reverse=True)
        print(sorted_mp)
        for i in sorted_mp:
            time = (target - i) / mp[i]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)