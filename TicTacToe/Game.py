from TicTacToe.Game_Board import GameBoard


class Game:
    def gameStart(self):
        self.controlBoard = GameBoard()
        self.gameBoard = self.controlBoard.gameBoard
        self.playerOne = 'O'
        self.playerTwo = 'X'
        print("Welcome to TikTakToe")
        print("Enter Player 1 Name")
        self.playerOne = input(" : ")
        print("Enter Player 2 Name")
        self.playerTwo = input(" : ")
        print("Here is your game board, each place is represented by 1-9, starting from left column and moving along "
              "the row")
        print(self.controlBoard.printBoard(self.gameBoard))
        self.turn = 1

    def gameEnd(self):
        if self.gameRunning == False:
            replay = input("Please press 0 to quit and 1 to continue: ")
            try:
                if int(replay):
                    self.gameRunning = True
                    self.gameStart()
            except:
                print("Use a number between 0 and 1")
                self.gameEnd()

    def takeTurn(self, user, item):
        print(user + "Please select the place from 1 to 9")
        try:
            position = int(input(": "))
            if position > 9 or position < 1:
                raise Exception
        except:
            print("Please enter number between 1 and 9")
            return self.takeTurn(user, item)

        if self.controlBoard.isPlaceTaken(self.gameBoard, position):
            print("The place is taken up")
            self.takeTurn(user, item)
        else:
            self.controlBoard.placeItems(item, position, self.gameBoard)
            self.controlBoard.printBoard(self.gameBoard)
            if self.controlBoard.isGameWon(self.gameBoard):
                print(user + " has won.")
                self.gameRunning = False

    def main(self, ):
        self.gameRunning = True
        self.gameStart()
        while self.gameRunning:
            if self.turn % 2 != 0:
                self.takeTurn(self.playerOne, "O")
            else:
                self.takeTurn(self.playerTwo, "X")

            if self.controlBoard.isBoardFull(self.gameBoard):
                print("Its a draw! You both lose")
                self.gameRunning = False
            self.turn += 1

            if not self.gameRunning:
                self.gameEnd()


if __name__ == '__main__':
    Game().main()
