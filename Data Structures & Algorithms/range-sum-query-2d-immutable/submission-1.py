class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cols = len(matrix[0])
        
        # 1. Start with a padding row of zeros
        self.prefix = [[0] * (cols + 1)]
        
        for i, row in enumerate(matrix):
            # 2. Start each row with a padding zero
            self.prefix.append([0])
            for j, elem in enumerate(row):
                # 3. self.prefix[i] is now the previous row (due to padding row)
                #    j+1 instead of j to account for padding col
                prefix_at_ij = sum(row[:j+1]) + self.prefix[i][j+1]
                self.prefix[i+1].append(prefix_at_ij)
      

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        whole = self.prefix[r2][c2]
        top_left = self.prefix[r1-1][c1-1]
        top = self.prefix[r1-1][c2]
        left = self.prefix[r2][c1-1]

        return whole - (top - top_left) - (left - top_left) - top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)