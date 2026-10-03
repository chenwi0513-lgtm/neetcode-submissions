class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {'(':')', '{': '}', '[': ']'}
        for x in s:
            if x in '{[(':
                l.append(x)
            else:
                if len(l) == 0:
                    return False
                if d[l[len(l)-1]] != x:
                    return False
                l.pop()
        if len(l) == 0:
            return True
        else:
            return False