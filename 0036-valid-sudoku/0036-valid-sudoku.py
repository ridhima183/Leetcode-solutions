class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            seen=set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        
        for col in range(9):
            seen=set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])


        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()

                for i in range(3):
                    for j in range(3):
                        value = board[box_row+i][box_col+j]

                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)

        return True
        