class GameBoard:
    def __init__(self):
        self.boardGame = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def placeItems(self, item, position, boardGame):
        boardGame[position] = item
        return boardGame

    @property
    def gameBoard(self):
        return self.boardGame

    def clearBoard(self):
        self.boardGame = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def isPlaceTaken(self, boardGame, index):
        if boardGame[index] != ' ':
            return True

    def isBoardFull(self, boardGame):
        for index in range(1, 10):
            if boardGame[index] == ' ':
                return False
        return True

    def isGameWon(self, boardGame):
        winCoords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for winCoord in winCoords:
            if boardGame[winCoord[0]] == boardGame[winCoord[1]] and boardGame[winCoord[1]] == boardGame[winCoord[2]] and \
                    boardGame[winCoord[0]] != ' ':
                return True

    def printBoard(self, boardGame):
        index = 0
        for row in range(1, 4):
            for column in range(1, 4):
                index += 1
                if column != 3:
                    print(boardGame[index], end='')
                    print("|", end='')
                else:
                    print(boardGame[index])
