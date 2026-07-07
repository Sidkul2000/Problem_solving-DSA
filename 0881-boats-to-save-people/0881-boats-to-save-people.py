class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boat = 0
        l, r = 0, n-1
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boat += 1
        return boat


        