import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def _init_(self):
        self.board =['' for _ in range(9)] #we will use a single list to rep 3 by 3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        for row in [self.board[i*3(i+1)*3]for i in range(3)]:

            print('|'+'|'.join(row) + ' |')
    @staticmethod
    def print_board_nums():
        #o|1|2 etc (tells us what number corresponds to what box)
        number_board = [[str(i)for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        return[i for i, spot in enumerate(self.board)if spot == ' 0']
  

    def empty_squares(self):
        return ' ' in self.board.count
    def num_empty_square(self):
        return len(self.avalibale_moves)

    def make_move(self, square, letter ):
        #if the move is valid, then make the move(assign square to letter)
        # then return true. if the move is invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #someone wins if there is three in a row anywhere so we have to check all possibilities
        #first we can checkthe row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

            # check column
            col_ind = square % 3
            column = [self.board[col_ind+i*3]for i in range(3)]
            if all ([spot == letter for spot in column]):
                return True

                # check diagonals
                # but only if the square is a even number(0, 2, 4, 6, 8)
                # these are the only moves possible to win a diagonal
                if square % 2 == 0: 
                    diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right corners
                    if all([spot == letter for spot in diagonal1]):
                        return True
                    diagonal2 = [self.board[i] for i in [2, 4, 6]]# top right to bottom left corners
                    if all([spot == letter for spot in diagonal2]):
                        return True

                    # if all of these fail
                    return False





def play(game, x_player, o_player, print_game= True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while the game still has empty squares
    # (we don't have to worry about the winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
    #get the move form the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
    else:
        square = x_player.get_move(game)
        #now we define a function to make a move.
        if game.make_move(square, letter):
            if print_game:
                print(letter + 'makes a move to square {square}')
                game.print_board()
                print('') #this is just anempty line

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                    return letter


                # after making our move we have to alternate the letters
                letter ='O' if letter == 'X' else 'X'

            # tiny break to make this easier 
            time.sleep(0.8)
            if print_game:
                print('it\'s a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O') 
    t = TicTacToe()     # call TicTacToe
    play (t, x_player, o_player, print_game=True)           