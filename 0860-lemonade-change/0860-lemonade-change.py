class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no5 = 0
        no10 = 0
        for bill in bills:
            if bill == 5:
                no5 += 1
            elif bill == 10:
                no10 += 1
                if no5 > 0:
                    no5 -= 1
                else:
                    return False
            else:
                if no10 > 0 and no5 > 0:
                    no10 -= 1
                    no5 -= 1
                elif no5 > 2:
                    no5 -= 3
                else:
                    return False
        return True

        