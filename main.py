import itertools


class SnakeGame(object):
    '''
    SnakeGame is a class that represents a snake game.

    Attributes:
    -----------
    rows: int
        number of rows in the board
    columns: int
        number of columns in the board
    snake: list of tuples
        list of tuples representing the snake
    board: list of lists
        list of lists representing the board
    directions: dict
        dictionary of directions

    Methods:
    --------
    add_snake:
        adds the snake to the board
    is_valid_move:
        checks if the movement is valid
    move_snake:
        moves the snake
    print_board:
        prints the board
    '''
    def __init__(self, rows, columns, snake):
        '''
        Initializes the SnakeGame class.

        Parameters:
        -----------
        rows: int
            number of rows in the board
        columns: int
            number of columns in the board
        snake: list of tuples
            list of tuples representing the snake
        '''
        self.rows = rows
        self.columns = columns
        self.snake = snake
        self.board = None
        self.directions = {'U': [0, -1],
                           'D': [0, 1],
                           'L': [-1, 0],
                           'R': [1, 0]}
        self.add_snake()

    def add_snake(self):
        '''
        Adds the snake to the board.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        '''
        self.board = [[0 for i in range(self.columns)]
                      for j in range(self.rows)]
        for i in range(len(self.snake)):
            self.board[self.snake[i][0]][self.snake[i][1]] = 1

    def is_valid_move(self, i, j, tail):
        '''
        Checks if the movement is valid.

        Parameters:
        -----------
        i: int
            row index of the new head
        j: int
            column index of the new head
        tail: list
            tail of the snake

        Returns:
        --------
        True if the movement is valid, False otherwise
        '''
        # check if the new head is out of bounds
        if (0 <= i < self.rows) and (0 <= j < self.columns):
            # check if the new head is the tail and not part of the snake
            if (not self.board[i][j]) or ([i, j] == tail):
                return True
        return False

    def move_snake(self, direction):
        '''
        Moves the snake.

        Parameters:
        -----------
        direction: str
            direction of the movement

        Returns:
        --------
        None
        '''
        movement = self.directions[direction]
        # get the head of the snake
        head = self.snake[0]
        tail = self.snake[-1]
        # get the new head of the snake
        new_head = [head[0] + movement[0], head[1] + movement[1]]
        # check if the new head is valid
        if self.is_valid_move(new_head[0], new_head[1], tail):
            # if valid, add the new head to the snake
            self.snake.insert(0, new_head)
            # remove the tail of the snake
            self.snake.pop()
            # add the new head to the board
            self.add_snake()
            return True
        return False

    def print_board(self):
        '''
        Prints the board.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        '''
        for i in range(self.columns):
            for j in range(self.rows):
                print(self.board[j][i], end=" ")
            print()
        print()


'''
Brute-force approach

All possible paths are tested, and only those that are feasible are taken as
good.

When implementing the following code as a function, it gave me problems when
creating the object of the SnakeGame class, so I have implemented it this way
so that it works for me.

The 3 test cases are tested below:

Test 1:
board: [4, 3]
snake: [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
depth: 3
Result: 7

Test 2:
board: [2, 3]
snake: [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
depth: 10
Result: 1

Test 3:
board: [10, 10]
snake: [[5,5], [5,4], [4,4], [4,5]]
depth: 4
Result: 81
'''

# TEST 1
all_combinations = ["".join(item)
                    for item in itertools.product("UDLR", repeat=3)]
total_paths = 0

for comb in all_combinations:
    snake_board = SnakeGame(rows=4,
                            columns=3,
                            snake=[[2, 2], [3, 2], [3, 1], [3, 0],
                                   [2, 0], [1, 0], [0, 0]])
    good_path = True

    for direction in comb:
        if not snake_board.move_snake(direction):
            good_path = False
            break

    if good_path:
        total_paths += 1

print(f'Result Test 1: {total_paths}')


# TEST 2
all_combinations = ["".join(item)
                    for item in itertools.product("UDLR", repeat=10)]
total_paths = 0

for comb in all_combinations:
    snake_board = SnakeGame(rows=2,
                            columns=3,
                            snake=[[0, 2], [0, 1], [0, 0], [1, 0], [1, 1],
                                   [1, 2]])
    good_path = True

    for direction in comb:
        if not snake_board.move_snake(direction):
            good_path = False
            break

    if good_path:
        total_paths += 1

print(f'Result Test 2: {total_paths}')


# TEST 3
all_combinations = ["".join(item)
                    for item in itertools.product("UDLR", repeat=4)]
total_paths = 0

for comb in all_combinations:
    snake_board = SnakeGame(rows=10,
                            columns=10,
                            snake=[[5, 5], [5, 4], [4, 4], [4, 5]])
    good_path = True

    for direction in comb:
        if not snake_board.move_snake(direction):
            good_path = False
            break

    if good_path:
        total_paths += 1

print(f'Result Test 3: {total_paths}')
