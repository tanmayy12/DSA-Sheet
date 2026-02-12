class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        flat = []
        for row in mat:
            for val in row:
                flat.append(val)

        result = []
        idx = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat[idx])
                idx += 1
            result.append(row)

        return result