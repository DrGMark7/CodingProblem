class Solution:
    def reverse(self, x: int) -> int:
        x_reverse = 0
        if x < 0:
            x_reverse = -1*int(str(x)[1:][::-1])
        elif x > 0:
            x_reverse = int(str(x)[::-1])
        else:
            return 0
        
        if x_reverse > 2147483648 or x_reverse < -2147483648:
            return 0
        return x_reverse