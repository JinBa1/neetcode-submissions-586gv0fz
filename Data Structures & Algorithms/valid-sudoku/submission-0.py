class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dim = 9
        rows = [set() for _ in range(dim)]
        cols = [set() for _ in range(dim)]
        sqr = [set() for _ in range(dim)]

        for row_id , r in enumerate(board):
            for col_id, n in enumerate(r):
                if n != ".":
                    sqr_id = (row_id // 3) * 3 + (col_id // 3)
                    if n in rows[row_id] or n in cols[col_id] or n in sqr[sqr_id]:
                        return False
                    else:
                        rows[row_id].add(n)
                        cols[col_id].add(n)
                        sqr[sqr_id].add(n)
        
        return True

