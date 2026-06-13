class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    box = (row//3,col//3)
                    if board[row][col] in rows[row]:
                        return False
                    else:
                        rows[row].append(board[row][col])
                    if board[row][col] in cols[col]:
                        return False
                    else:
                        cols[col].append(board[row][col])
                    if board[row][col] in boxes[box]:
                        return False
                    else:
                        boxes[box].append(board[row][col])
        return True
                    