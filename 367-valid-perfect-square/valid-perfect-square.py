class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if len(str(num**0.5).split(".")[-1]) == 1:
            return True
        else:
            return False