class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for l in logs:
            if l.split()[1].isalpha():
                letters.append(l)
            else:
                digits.append(l)
        letters.sort(key = lambda x : x.split(" ")[0])
        letters.sort(key = lambda x : x.split(" ")[1:])
        return letters + digits

            