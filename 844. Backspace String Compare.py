class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        if s == t:
            return True
        for i in range(len(s)):
            if s[i] != '#':
                stack.append(s[i])
            elif len(stack) != 0:
                stack.pop()
        
        for j in range(len(t)):
            if t[j] != '#':
                stack2.append(t[j])
            elif len(stack2) != 0:
                stack2.pop()
        print(stack)
        print(stack2)
        return stack == stack2
        