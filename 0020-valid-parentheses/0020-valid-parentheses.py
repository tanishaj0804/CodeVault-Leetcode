class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack =[]
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0

        