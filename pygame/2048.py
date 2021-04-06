# imports
import pygame, random, sys
pygame.init()

# game information
score = 0
grid = 64
width = 4
height = 4
board = []
roboto = pygame.font.SysFont('Roboto', grid // 2)
white = (255, 255, 255)
black = (0, 0, 0)

# updates caption
def update_caption():
    pygame.display.set_caption('Score: ' + str(score))

# initialize screen
screen_size = (width * grid, height * grid)
screen = pygame.display.set_mode(screen_size)
update_caption()

# initialize board
for x in range(width):
    col = []
    for y in range(height):
        col.append('.')
    board.append(col)

# draws board to screen
def draw_board():
    screen.fill(white)
    for x in range(width):
        for y in range(height):
            # skip empty tiles
            if board[x][y] == '.': continue
            tile = board[x][y]
            pos = (x * grid, y * grid)
            rect = (pos, (grid, grid))
            color = (0, 0, 255 - (tile % 256))
            pygame.draw.rect(screen, color, rect)
            text_surface = roboto.render(str(tile), False, black)
            screen.blit(text_surface, pos)
    pygame.display.update()

# spawn tile at random location
def spawn_tile():
    # if no empty spaces, return
    if not any('.' in line for line in board): return
    # 2 or 4
    tile = random.randint(1, 2) * 2
    # get random position
    rand_x = random.randint(0, width - 1)
    rand_y = random.randint(0, height - 1)
    # while tile not empty
    while board[rand_x][rand_y] != '.':
        # get random position
        rand_x = random.randint(0, width - 1)
        rand_y = random.randint(0, height - 1)
    # update board
    board[rand_x][rand_y] = tile

# game over
def gameover():
    print('Game over')
    print('Final score: ' + str(score))
    pygame.quit()
    sys.exit()

# checks whether game over
def check_gameover():
    # if any empty spaces, return
    if any('.' in line for line in board): return
    for x in range(width):
        for y in range(height):
            tile = board[x][y]
            # if any adjacent same tiles, return
            if x > 0 and board[x - 1][y] == tile: return
            if x < width - 1 and board[x + 1][y] == tile: return
            if y > 0 and board[x][y - 1] == tile: return
            if y < height - 1 and board[x][y + 1] == tile: return
    gameover()

# shift board in given direction
def shift_board(dr):
    global score
    moved = False
    # up
    if dr == 'w':
        for x in range(width):
            for y in range(1, height):
                if board[x][y] == '.': continue
                yy = y - 1; nxt = board[x][yy]
                if nxt != '.' and nxt != board[x][y]: continue
                moved = True
                while yy > 0 and board[x][yy] == '.': yy -= 1
                if board[x][yy] == '.': board[x][yy] = board[x][y]
                elif board[x][yy] == board[x][y]:
                    board[x][yy] *= 2
                    score += board[x][yy]
                else: board[x][yy + 1] = board[x][y]
                board[x][y] = '.'
    # left
    elif dr == 'a':
        for y in range(height):
            for x in range(1, width):
                if board[x][y] == '.': continue
                xx = x - 1; nxt = board[xx][y]
                if nxt != '.' and nxt != board[x][y]: continue
                moved = True
                while xx > 0 and board[xx][y] == '.': xx -= 1
                if board[xx][y] == '.': board[xx][y] = board[x][y]
                elif board[xx][y] == board[x][y]:
                    board[xx][y] *= 2
                    score += board[xx][y]
                else: board[xx + 1][y] = board[x][y]
                board[x][y] = '.'
    # down
    elif dr == 's':
        for x in range(width):
            for y in range(height - 2, -1, -1):
                if board[x][y] == '.': continue
                yy = y + 1; nxt = board[x][yy]
                if nxt != '.' and nxt != board[x][y]: continue
                moved = True
                while yy < height - 1 and board[x][yy] == '.': yy += 1
                if board[x][yy] == '.': board[x][yy] = board[x][y]
                elif board[x][yy] == board[x][y]:
                    board[x][yy] *= 2
                    score += board[x][yy]
                else: board[x][yy - 1] = board[x][y]
                board[x][y] = '.'
    # right
    elif dr == 'd':
        for y in range(height):
            for x in range(width - 2, -1, -1):
                if board[x][y] == '.': continue
                xx = x + 1; nxt = board[xx][y]
                if nxt != '.' and nxt != board[x][y]: continue
                moved = True
                while xx < width - 1 and board[xx][y] == '.': xx += 1
                if board[xx][y] == '.': board[xx][y] = board[x][y]
                elif board[xx][y] == board[x][y]:
                    board[xx][y] *= 2
                    score += board[xx][y]
                else: board[xx - 1][y] = board[x][y]
                board[x][y] = '.'
    # if board shifted, spawn new tile
    if moved: spawn_tile()

# updates with given direction input
def update(dr):
    # shift by user input
    shift_board(dr)
    # draw board
    draw_board()
    # update caption
    update_caption()
    # check gameover
    check_gameover()

# game loop
clock = pygame.time.Clock()
spawn_tile()
draw_board()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            gameover()
        # update with input direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: update('w')
            elif event.key == pygame.K_a: update('a')
            elif event.key == pygame.K_s: update('s')
            elif event.key == pygame.K_d: update('d')
