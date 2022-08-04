import itertools

class SnakeGame:
    def __init__(self, rows, columns, snake):
        self.rows = rows
        self.columns = columns
        self.snake = snake
        self.directions = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}
        self.add_snake()

    def add_snake(self):
        self.board = [[0 for i in range(self.columns)] for j in range(self.rows)]
        for i in range(len(self.snake)):
            self.board[self.snake[i][0]][self.snake[i][1]] = 1

    def is_valid_move(self, i, j):
        if (0 <= i < self.rows) and (0 <= j < self.columns):
            if not self.board[i][j]:
                return True
        return False

    def move_snake(self, direction):
        movement = self.directions[direction]
        # get the head of the snake
        head = self.snake[0]
        # get the new head of the snake
        new_head = [head[0] + movement[0], head[1] + movement[1]]
        # check if the new head is valid
        if self.is_valid_move(new_head[0], new_head[1]):
            # if valid, add the new head to the snake
            self.snake.insert(0, new_head)
            # remove the tail of the snake
            self.snake.pop()
            # add the new head to the board
            self.add_snake()
            return True

        return False

    def print_board(self):
        for i in range(self.columns):
            for j in range(self.rows):
                print(self.board[j][i], end=" ")
            print()
        print()


board = SnakeGame(4, 3, [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]])
board.print_board()
print(board.move_snake('L'))
board.print_board()

# depth = 2
# all_combinations = ["".join(item) for item in itertools.product("UPLR", repeat=depth)]

# for comb in all_combinations:
#     for c in comb:
#         print(c)


