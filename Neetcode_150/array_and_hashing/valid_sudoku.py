from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for i in range(len(board)):
            for j in range(len(board)):

                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if (i//3,j//3) not in boxes:
                    boxes[(i//3,j//3)] = set()

                if board[i][j] == '.':
                    continue

                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])

                if board[i][j] in boxes[(i//3,j//3)]:
                    return False
                boxes[(i//3,j//3)].add(board[i][j])

        return True


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.isValidSudoku(board= [["5","3",".",".","7",".",".",".","."]
                                 ,["6",".",".","1","9","5",".",".","."]
                                 ,[".","9","8",".",".",".",".","6","."]
                                 ,["8",".",".",".","6",".",".",".","3"]
                                 ,["4",".",".","8",".","3",".",".","1"]
                                 ,["7",".",".",".","2",".",".",".","6"]
                                 ,[".","6",".",".",".",".","2","8","."]
                                 ,[".",".",".","4","1","9",".",".","5"]
                                 ,[".",".",".",".","8",".",".","7","9"]]
                            )
          )

    print(
        sol.isValidSudoku(board= [["8","3",".",".","7",".",".",".","."]
                                 ,["6",".",".","1","9","5",".",".","."]
                                 ,[".","9","8",".",".",".",".","6","."]
                                 ,["8",".",".",".","6",".",".",".","3"]
                                 ,["4",".",".","8",".","3",".",".","1"]
                                 ,["7",".",".",".","2",".",".",".","6"]
                                 ,[".","6",".",".",".",".","2","8","."]
                                 ,[".",".",".","4","1","9",".",".","5"]
                                 ,[".",".",".",".","8",".",".","7","9"]]
                            )
          )