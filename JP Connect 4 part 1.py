class Connect_Four():
    Col_Count = 7 #amount of columns
    Row_Count = 6 #amount of rows
    def __init__(self):
        self.board = [[' ' for num in range(Connect_Four.Col_Count)] for rows in range(Connect_Four.Row_Count)]

    def print_board(self): #Prints the current connect4 board, complete with placed pieces
        result = ''
        for rows in self.board:
            result += '-' * 15 + '\n' #places -'s 15 times in each row for the amount of rows there are in the game
            for col in rows:
                result += f'|{col}'
            result += '|\n' #goes down a line after making |
        print(result) #prints board

    def drop(self, col, team: str): #  Drops a piece into the connect 4 board at the selected column and fills the position with the chosen team character
       
        if col: 
            if col.isdigit():
                col = int(col)
                if col <= 7 and col > -1 or col == None: #the col must be an int between 1-7
                    col -= 1
                    if self.board[0][col] == ' ':
                        for num in range(5, -1, -1):
                            if self.board[num][col] == ' ':
                                self.board[num][col] = team
                                break
                    else:
                        print("That column is full. Your turn is skipped (be more careful next time)")
                else:
                    print("You need to put it on the board... choose a number 1-7 next time. You lost your turn")
            else:
                print("That wasnt even a number... You lose your turn.")
        else:
            print("That wasnt even a number OR a letter... Place somewhere next time :/  You lose your turn.")

    def check(self, team: str): #checks the cross section for each point on the board. Checks it vertically, horizontally, and diagonally right and left. 
        for col in range(Connect_Four.Col_Count-3):# check horizontal wins
            for row in range(Connect_Four.Row_Count):
                 #checks for the same value in the same column
                if self.board[row][col] == team and self.board[row][col+1] == team and self.board[row][col+2] == team and self.board[row][col+3] == team:
                    return True
        for col in range(Connect_Four.Col_Count):# check for vertical wins
            for row in range(Connect_Four.Row_Count-3):
                #checks for the same value in the same row
                if self.board[row][col] == team and self.board[row+1][col] == team and self.board[row+2][col] == team and self.board[row+3][col] == team:
                    return True
        for col in range(Connect_Four.Col_Count-3):# check for diagonal right wins
            for row in range(Connect_Four.Row_Count-3):
                #checks for the same value going up and to the right once
                if self.board[row][col] == team and self.board[row+1][col+1] == team and self.board[row+2][col+2] == team and self.board[row+3][col+3] == team:
                    return True
        for col in range(Connect_Four.Col_Count-4, Connect_Four.Col_Count):# check for diagonal left wins
            for row in range(Connect_Four.Row_Count-3):
                #checks for the same value going down and to the right once
                if self.board[row][col] == team and self.board[row+1][col-1] == team and self.board[row+2][col-2] == team and self.board[row+3][col-3] == team:
                    return True

    def draw_check(self): #checking for draws by seeing if every space is filled. If there is a ' ' (blank space) then it returns false. 
        for sections in self.board:
            for spaces in sections:
                if spaces == ' ':
                    return False
        return True

if __name__ == '__main__':
    board = Connect_Four()
    team1, team2 = '', ''
    print("Welcome to Connect 4!")
    while len(team1) != 1:
        team1 = "X"

    while len(team2) != 1:
        team2 = "O"
        '''if team2 == team1:
            print("How are you going to tell who is who? Play again and this time don't pick matching symbols :) ") 
            quit()'''
            
    board.print_board()

    while not board.check(team1) and not board.check(team2):
        col = input(f"Player 1 ({team1}) place a piece in columns (1-7): ")
        board.drop(col, team1) #drops a piece for the first team in the chosen column
        board.print_board() #print the updated board out

        if board.check(team1): # if the board check for player one goes through they win!
            print(f"PLAYER 1 ({team1}) WON!") 
            quit()

        if board.draw_check(): #if after their turn the board is full, they draw
            print("It's a draw")
            quit()

        col = input(f"Player 2 ({team2}) place a piece in columns (1-7): ") 
        board.drop(col, team2)#drops a piece for the first team in the chosen column
        board.print_board()

        if board.check(team2):
            print(f"PLAYER 2 ({team2}) WON!")
            quit()
