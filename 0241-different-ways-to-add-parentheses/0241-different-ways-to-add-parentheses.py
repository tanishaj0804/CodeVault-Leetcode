class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]
        result = []
        for i,char in enumerate(expression):
            if char in"+-*":
                leftsub = self.diffWaysToCompute(expression[:i])
                rightsub = self.diffWaysToCompute(expression[i+1:])
                for l in leftsub:
                    for r in rightsub:
                        if char == "+":
                            result.append(l+r)
                        elif char == '-':
                            result.append(l-r)
                        else:
                            result.append(l*r)
        return result


        