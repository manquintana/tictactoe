class Tictactoe():
    
    DIMENSION = 3

    def __init__(self, players):
        self._tablero = []
        for i in range(Tictactoe.DIMENSION):
            self._tablero.append(['-', '-', '-'])
        self._turno = True # True -> o / False -> x
        self._winner = None
        self._player_o = players[0]
        self._player_x = players[1]
        #self._player_names(names)
        #print(self._tablero)

    def __str__(self):
        # Graphic board string
        row_separator = '+---+---+---+\n'
        graphic_board = '=TIC TAC TOE=\n' + row_separator
        for row in range(Tictactoe.DIMENSION):
            current_row = ''
            for column in range(Tictactoe.DIMENSION):
                current_row += f'| {self._tablero[row][column]} '
            graphic_board += current_row + '|\n' + row_separator
        # Next turn string
        next_string = self._check_winner()
        #next_string = f'{self.who_is_next()}'
        return graphic_board + next_string + '\n'

    def __repr__(self):
        # Graphic board string
        row_separator = '+---+---+---+\n'
        graphic_board = '=TIC TAC TOE=\n' + row_separator
        for row in range(Tictactoe.DIMENSION):
            current_row = ''
            for column in range(Tictactoe.DIMENSION):
                current_row += f'| {self._tablero[row][column]} '
            graphic_board += current_row + '|\n' + row_separator
        # Line status string
        repr_string =f'Row check: {self.check_row_col("row")}\nCol check: {self.check_row_col("col")}\nDiag check: {self.check_diag()}\n'
        # Next turn string
        next_string = f'{self.who_is_next()}'
        return graphic_board + repr_string + next_string
    # --------------
    # Public methods
    # --------------
    def move(self, position):
        row, column = position[0], position[1]
        if (self._tablero[row][column] == '-'):
            if (self._turno):
                self._tablero[row][column] = 'o'
            else:
                self._tablero[row][column] = 'x'
            self._turno = not(self._turno)
        else:
            raise ValueError(f'Position ({row},{column}) has already been taken')
    
    def who_is_next(self):
        if self._get_turn():
            sentence = f'It\'s player {self._get_player_o()}\'s turn'
        else:
            sentence = f'It\'s player {self._get_player_x()}\'s turn'
        return sentence

    # --------------
    # Private methods
    # --------------
    def _get_val(self, row, col):
        try:
            return(self._tablero[row][col])
        except:
            raise ValueError('Indexes out of range! they must be < DIMENSION')
    
    def _get_player_o(self):
        return self._player_o

    def _get_player_x(self):
        return self._player_x

    def _get_row(self, index):
        try:
            return self._tablero[index]
        except:
            raise ValueError('Index out of range! It must be < DIMENSION')

    def _get_col(self, index):
        try:
            if (index < Tictactoe.DIMENSION):
                column = []
                for r in range(Tictactoe.DIMENSION):
                    column.append(self._tablero[r][index])
                return column
        except:
                raise ValueError('Index out of range! It must be < DIMENSION')

    def _get_diag(self, diagonal_1_2): # diag 0 --> \, diag 0 --> /
        diagonal = []
        if diagonal_1_2 == 0: # Diagonal 0 --> \
            for d in range(Tictactoe.DIMENSION):
                diagonal.append(self._get_val(d,d))
        else: # Diagonal 1 --> /
            end = Tictactoe.DIMENSION - 1 
            start = 0
            while (end >= 0):
                diagonal.append(self._get_val(end, start))
                end -= 1
                start += 1
        return diagonal

    def _get_turn(self):
        return self._turno

    def check_row_col(self, row_col):
        status = []
        for i in range(Tictactoe.DIMENSION):
            if (row_col == 'row'):
                current_line = self._get_row(i)
            else:
                current_line = self._get_col(i)
            if (len(set(current_line)) == 1) and (current_line[0] != '-'):
                status.append(current_line[0])
            else:
                status.append('-')
        return status
    
    def check_diag(self):
        status = [] # diag 0 --> \, diag 1 --> /
        for i in range(2): #There are 2 possible diagonals
            diag = self._get_diag(i)
            if (len(set(diag)) == 1) and (diag[0] != '-'):
                status.append(diag[0])
            else:
                status.append('-')
        return status

    def _check_winner(self):
        if ('o' in self.check_diag()) or ('o' in self.check_row_col('row')) or ('o' in self.check_row_col('col')):
            string = 'o is the WINNER!'
            self._winner = 'o'
        else:
            if ('x' in self.check_diag()) or ('x' in self.check_row_col('row')) or ('x' in self.check_row_col('col')):
                string = 'x is the WINNER!'
                self._winner = 'x'
            else: #Check tie!
                all_values = []
                for i in range(0, Tictactoe.DIMENSION):
                    for j in range(0, Tictactoe.DIMENSION):
                        all_values.append(self._get_val(i,j))
                    print(f'Fullrows: {all_values}')
                if ('-' not in all_values):
                    string = 'Tie! Game over'
                    self._winner = 'tie'
                else:
                    string = self.who_is_next()
        return string

    def get_winner(self):
        return self._winner


players = ['Manuel', 'Alejandro']
juego = Tictactoe(players)
print(str(juego))

while (juego.get_winner() is None):
    print('Make your move')
    try:
        row = int(input('Input desired row (1,2,3): '))
        col = int(input('Input desired col (1,2,3): '))
        juego.move([row-1, col-1])
    except ValueError as v:
        print(str(v))
        
    print(str(juego))

