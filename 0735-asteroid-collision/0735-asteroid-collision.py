class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if stack[-1] == -asteroids[i]: 
                    stack.pop()
                    break
                elif stack[-1] < -asteroids[i]:
                    stack.pop()
                    continue
                elif stack[-1] > -asteroids[i]:
                    break
            else:
                stack.append(asteroids[i])

        return stack
            
        