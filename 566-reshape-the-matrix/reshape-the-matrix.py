class Solution(object):
    def matrixReshape(self, mat, r, c):
        if len(mat[0])*len(mat) == r*c:
            Array_1D = []
            for i in mat:
                for j in i:
                    Array_1D.append(j)
            New_array = []
            for i in range(r):
                New_row = []
                for j in range(c):
                    New_row.append(Array_1D[(i*c)+j])
                New_array.append(New_row)

            return New_array
        else:
            return mat
        
        
        