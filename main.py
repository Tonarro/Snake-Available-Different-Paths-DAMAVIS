import itertools

class SnakeGame(object):

    def __init__(self, rows, columns, snake):
        self.rows = rows
        self.columns = columns
        self.snake = snake
        self.board = None
        self.directions = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}
        self.add_snake()


    def add_snake(self):
        self.board = [[0 for i in range(self.columns)] for j in range(self.rows)]
        for i in range(len(self.snake)):
            self.board[self.snake[i][0]][self.snake[i][1]] = 1

    def is_valid_move(self, i, j, tail):
        # check if the new head is out of bounds
        if (0 <= i < self.rows) and (0 <= j < self.columns):
            # check if the new head is the tail and not part of the snake 
            if (not self.board[i][j]) or ([i, j] == tail):
                return True
        return False

    def move_snake(self, direction):
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
        for i in range(self.columns):
            for j in range(self.rows):
                print(self.board[j][i], end=" ")
            print()
        print()



all_combinations = ["".join(item) for item in itertools.product("UDLR", repeat=4)]
total_paths = 0

for comb in all_combinations:
    board = SnakeGame(10, 10, [[5,5], [5,4], [4,4], [4,5]])
    good_path = True

    for direction in comb:
        if not board.move_snake(direction):
            good_path = False
            break
    
    if good_path:
        total_paths += 1

print(total_paths)
