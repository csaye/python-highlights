### imports ###

import pygame, sys

### globals ###

update = 10
grid = 16
screen_x = 32; screen_y = 32
score_a = 0; score_b = 0
paddle_size = int(0.25 * screen_y)
paddle_offset = 2

white = (255, 255, 255)
black = (0, 0, 0)

### screen ###

# updates caption with current scores
def update_caption():
    caption = str(score_a) + ' | ' + str(score_b)
    pygame.display.set_caption(caption)

# initialize screen and update caption
screen_size = (screen_x * grid, screen_y * grid)
screen = pygame.display.set_mode(screen_size)
update_caption()

### board ###

# draws current board to screen
def draw_board():
    screen.fill(black)
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            # if board filled
            if board[x][y] == 1:
                # draw rect
                rect = ((x * grid, y * grid), (grid, grid))
                pygame.draw.rect(screen, white, rect)
    pygame.display.update()

# initialize board
board = []
for y in range(0, screen_y):
    row = []
    for x in range(0, screen_x):
        row.append(0)
    board.append(row)

### paddles ###

take_input_a = True; take_input_b = True
paddle_a_top = int(screen_y / 2) - int(paddle_size / 2)
paddle_b_top = int(screen_y / 2) - int(paddle_size / 2)

# initialize paddles
for y in range(int(screen_y / 2) - int(paddle_size / 2),
               int(screen_y / 2) + int(paddle_size / 2)):
    board[paddle_offset][y] = 1
    board[screen_x - paddle_offset - 1][y] = 1

def paddle_input_a(direction):
    global paddle_a_top, take_input_a
    # if not taking input, return
    if not take_input_a: return
    if direction == 'up':
        # if out of bounds, return
        if paddle_a_top <= 0: return
        # move paddle and stop take input
        paddle_a_top -= 1
        board[paddle_offset][paddle_a_top] = 1
        board[paddle_offset][paddle_a_top + paddle_size] = 0
        take_input_a = False
    elif direction == 'down':
        # if out of bounds, return
        if paddle_a_top >= screen_y - paddle_size: return
        # move paddle and stop take input
        paddle_a_top += 1
        board[paddle_offset][paddle_a_top - 1] = 0
        board[paddle_offset][paddle_a_top + paddle_size - 1] = 1
        take_input_a = False

def paddle_input_b(direction):
    global paddle_b_top, take_input_b
    # if not taking input, return
    if not take_input_b: return
    if direction == 'up':
        # if out of bounds, return
        if paddle_b_top <= 0: return
        # move paddle and stop take input
        paddle_b_top -= 1
        board[screen_x - paddle_offset - 1][paddle_b_top] = 1
        board[screen_x - paddle_offset - 1][paddle_b_top + paddle_size] = 0
        take_input_b = False
    elif direction == 'down':
        # if out of bounds, return
        if paddle_b_top >= screen_y - paddle_size: return
        # move paddle and stop take input
        paddle_b_top += 1
        board[screen_x - paddle_offset - 1][paddle_b_top - 1] = 0
        board[screen_x - paddle_offset - 1][paddle_b_top + paddle_size - 1] = 1
        take_input_b = False

### ball ###

# initialize ball
ball_x = int(screen_x / 2); ball_y = int(screen_y / 2)
ball_dir = 'ur' # ur, dr, dl, ul
board[ball_x][ball_y] = 1

def move_ball():
    global ball_x, ball_y, ball_dir, score_a, score_b

    if ball_dir == 'ur':
        # recurse if bouncing
        if ball_y <= 0 or board[ball_x][ball_y - 1] == 1:
            ball_dir = 'dr'
            move_ball()
        elif ball_x >= screen_x - 1 or board[ball_x + 1][ball_y] == 1:
            ball_dir = 'ul'
            move_ball()
        # if clear, move
        else:
            board[ball_x][ball_y] = 0
            ball_x += 1; ball_y -= 1
            if ball_x <= 0: score_b += 1
            elif ball_x >= screen_x - 1: score_a += 1
            board[ball_x][ball_y] = 1

    elif ball_dir == 'dr':
        # recurse if bouncing
        if ball_y >= screen_y - 1 or board[ball_x][ball_y + 1] == 1:
            ball_dir = 'ur'
            move_ball()
        elif ball_x >= screen_x - 1 or board[ball_x + 1][ball_y] == 1:
            ball_dir = 'dl'
            move_ball()
        # if clear, move
        else:
            board[ball_x][ball_y] = 0
            ball_x += 1; ball_y += 1
            if ball_x <= 0: score_b += 1
            elif ball_x >= screen_x - 1: score_a += 1
            board[ball_x][ball_y] = 1

    elif ball_dir == 'dl':
        # recurse if bouncing
        if ball_y >= screen_y - 1 or board[ball_x][ball_y + 1] == 1:
            ball_dir = 'ul'
            move_ball()
        elif ball_x <= 0 or board[ball_x - 1][ball_y] == 1:
            ball_dir = 'dr'
            move_ball()
        # if clear, move
        else:
            board[ball_x][ball_y] = 0
            ball_x -= 1; ball_y += 1
            if ball_x <= 0: score_b += 1
            elif ball_x >= screen_x - 1: score_a += 1
            board[ball_x][ball_y] = 1

    elif ball_dir == 'ul':
        # recurse if bouncing
        if ball_y <= 0 or board[ball_x][ball_y - 1] == 1:
            ball_dir = 'dl'
            move_ball()
        elif ball_x <= 0 or board[ball_x - 1][ball_y] == 1:
            ball_dir = 'ur'
            move_ball()
        # if clear, move
        else:
            board[ball_x][ball_y] = 0
            ball_x -= 1; ball_y -= 1
            if ball_x <= 0: score_b += 1
            elif ball_x >= screen_x - 1: score_a += 1
            board[ball_x][ball_y] = 1

### main ###

# time tracking
clock = pygame.time.Clock()
frame = 0

# game loop
draw_board()
while True:

    # tick
    clock.tick(60)
    frame += 1

    # events
    for event in pygame.event.get():

        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: paddle_input_a('up')
            if event.key == pygame.K_s: paddle_input_a('down')
            if event.key == pygame.K_UP: paddle_input_b('up')
            if event.key == pygame.K_DOWN: paddle_input_b('down')

    # update
    if frame % update == 0:

        # move ball
        move_ball()

        # draw board
        draw_board()

        # update caption
        update_caption()

        # reset take input
        take_input_a = True; take_input_b = True
