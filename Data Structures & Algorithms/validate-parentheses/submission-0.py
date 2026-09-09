class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        map = {")":"(","]":"[","}":"{"}
        stack = []

        for char in s:
            if char in map:
                x = stack.pop() or "#" if stack else "#"
                if map[char] != x:
                    return False
            
            else:
                stack.append(char)
        return len(stack)==0