class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            if b==5:
                fives+=1
            if b==10:
                tens+=1
            change = b-5                
            if change == 5: #paid with 10
                if fives>0:
                    fives-=1
                else:
                    return False
            if change == 15: #paid with 20
                if fives>0 and tens>0:
                    fives-=1
                    tens-=1
                elif fives>2:
                    fives -=3
                else:
                    return False
        return True