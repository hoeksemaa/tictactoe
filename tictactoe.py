import os

class ttt:
    def __init__(self):
        self.board = [
                [" ", " ", " "], 
                [" ", " ", " "], 
                [" ", " ", " "]]
        self.game_over = False

    def check_valid_move(self, row, column):
        if self.board[row][column] == " ":
            return True
        else:
            return False

    def play_turn(self, character, row, column):
        self.board[row][column] = character    

    def print_board(self):
        print(" {} | {} | {} ".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("---+---+----")
        print(" {} | {} | {} ".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("---+---+----")
        print(" {} | {} | {} ".format(self.board[2][0], self.board[2][1], self.board[2][2]))

    def check_for_win(self):
        # row check
        for row in self.board: 
            if len(set(row)) == 1 and row[0] != " ":
                return row[0]

        # column check
        for col in range(3):
            if len(set([self.board[row][col] for row in range(3)])) == 1 and self.board[0][col] != " ":
                return self.board[0][col]

        # diagonal check
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[1][1]

        # diagonal check
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            return self.board[1][1]

        return None

def get_character():
    character = input("> what character will you play?: ") 
    while len(character) > 1:
        print("Please select a single character")
        character = input("> what character will you play?: ")
    return character

def is_valid_number(character):
    try:
        num = int(character)
        if num >= 0 and num <= 2:
            return True
        else:
            return False
    except:
        return False

def get_row():
    row = input("> what row will you play in (0, 1, 2)?: ")
    while not is_valid_number(row):
        print("please enter a number between 0 and 2")
        row = input("> what row will you play in (0, 1, 2)?: ")
    return int(row)

def get_column():
    column = input("> what column will you play in (0, 1, 2)?: ")
    while not is_valid_number(column):
        print("please enter a number between 0 and 2")
        column = input("> what column will you play in (0, 1, 2)?: ")
    return int(column)

def get_position(board):
    row = get_row()
    column = get_column()
    while not board.check_valid_move(row, column):
        print("please select an empty row and column to play in")
        row = get_row()
        column = get_column()
    return row, column
    
def main():
    board = ttt()
    os.system('cls' if os.name == 'nt' else 'clear')
    board.print_board()
    while not board.check_for_win():
        character = get_character()
        row, column = get_position(board)
        board.play_turn(character, row, column)
        os.system('cls' if os.name == 'nt' else 'clear')
        board.print_board()
        if board.check_for_win():
            print("Player {} wins!".format(board.check_for_win()))

if __name__ == "__main__":
    main()

