#My solution, ideal solution
#O(n*m*4^len(word)) time, O(len(word)) space
class Solution:
    
    #Strategy: Loop through board, performing search algorithm if the current sqaure is the first letter of the word (essentially performing a DFS)
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > (len(board) * len(board[0])):
            return False
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    if (self.search(board, word, 0, i, j)):
                        return True
        return False
       
    #Here, we store the current board position, the board, the word, and the index we are at on the word
    #We check each square. If the value is equal to the word at the current pos, and the current pos is the last letter, return True, as we've found the word
    #Else, we set that sqaure to '#', and check the four surrounding spots
    #Note that '#' indicates to following calls that that sqaure has been visited, and can not be used again
    #After the calls are done, the original value is restored
    def search(self, board, word, pos, i, j):
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1:
            return False
        if word[pos] != board[i][j]:
            return False
        else:
            if pos == len(word) - 1:
                return True
            pos += 1
            temp = board[i][j]
            board[i][j] = '#'
            valid = self.search(board, word, pos, i, j + 1) or self.search(board, word, pos, i, j - 1) or self.search(board, word, pos, i + 1, j) or self.search(board, word, pos, i - 1, j)
            board[i][j] = temp
            return valid
