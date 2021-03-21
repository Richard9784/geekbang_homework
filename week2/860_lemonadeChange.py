class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills and (bills[0] == 10 or bills[0] == 20):return False
        res = collections.defaultdict(int)
        for x in bills:
            if x == 10:
                if res[5]>=1:
                    res[5] -= 1
                else:
                    return False
            elif x == 20:
                if res[10] >= 1 and res[5] >= 1:
                    res[10] -= 1
                    res[5] -= 1
                elif res[5]>=3:
                    res[5] -= 3
                else:
                    return False
            res[x] += 1
        return True
                

