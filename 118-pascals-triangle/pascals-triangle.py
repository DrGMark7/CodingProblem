class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def factorial(n):
            x = 1
            for i in range(n):
                x *= (i+1)
            return x

        def nCr(n,r):
            return (factorial(n))/(factorial(r)*factorial(n-r))

        result = [[1]]
        for i in range(1,numRows):
            temp = []
            for j in range(i+1):
                temp.append(int(nCr(i,j)))
            result.append(temp)

        return result