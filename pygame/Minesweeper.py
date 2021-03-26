import pygame, sys, random
pygame.init()

### globals ###

# screen
grid = 32
screen_x = 16; screen_y = 16

# game
mine_chance = 0.1
game_over = False
mines = 0
flags = 0

# colors
white = (255, 255, 255)
gray = (240, 240, 240)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# fonts
roboto = pygame.font.SysFont('Roboto', grid)

### screen ###

# sets caption to given text
def set_caption(caption):
    pygame.display.set_caption(caption)

# initialize screen
screen_size = (screen_x * grid, screen_y * grid)
screen = pygame.display.set_mode(screen_size)
set_caption('Minesweeper')

### board ###

# initialize board
board = []
revealed = []
for x in range(screen_x):
    col = []
    r_col = []
    for y in range(screen_y):
        # draw rect
        rect = ((x * grid, y * grid), (grid, grid))
        color = white if (x + y) % 2 == 0 else gray
        pygame.draw.rect(screen, color, rect)
        r_col.append(False)
        # generate mine or number
        if random.random() < mine_chance:
            col.append('m')
            mines += 1
        else: col.append(0)
    board.append(col)
    revealed.append(r_col)
pygame.display.update()
# initialize numbers
for x in range(screen_x):
    for y in range(screen_y):
        # if mine, continue
        if board[x][y] == 'm': continue
        xa = 0 if x == 0 else x - 1
        ya = 0 if y == 0 else y - 1
        xb = screen_x - 1 if x == screen_x - 1 else x + 1
        yb = screen_y - 1 if y == screen_y - 1 else y + 1
        # check around square
        for x2 in range(xa, xb + 1):
            for y2 in range(ya, yb + 1):
                # skip self
                if x2 == x and y2 == y: continue
                # if mine, increment self
                if board[x2][y2] == 'm': board[x][y] += 1

# draws given tile
def draw(x, y):
    # draw rect
    rect = ((x * grid, y * grid), (grid, grid))
    color = white if (x + y) % 2 == 0 else gray
    pygame.draw.rect(screen, color, rect)
    # if not revealed, return
    if revealed[x][y] == False: return
    # get char of tile
    char = 'f' if revealed[x][y] == 'f' else str(board[x][y])
    # blit text
    text_color = black
    if revealed[x][y] == 'f': text_color = blue
    elif board[x][y] == 'm': text_color = red
    text_surface = roboto.render(char, False, text_color)
    text_pos = (x * grid, y * grid)
    screen.blit(text_surface, text_pos)

# recursively reveals board, starting from given tile
def recursive_reveal(x, y):
    global flags
    # reveal adjacent tiles
    xa = 0 if x == 0 else x - 1
    ya = 0 if y == 0 else y - 1
    xb = screen_x - 1 if x == screen_x - 1 else x + 1
    yb = screen_y - 1 if y == screen_y - 1 else y + 1
    for x2 in range(xa, xb + 1):
        for y2 in range(ya, yb + 1):
            # skip self
            if x2 == x and y2 == y: continue
            # if zero, recurse
            if board[x2][y2] == 0 and revealed[x2][y2] != True:
                if revealed[x2][y2] == 'f': flags -= 1
                revealed[x2][y2] = True
                draw(x2, y2)
                recursive_reveal(x2, y2)
            else:
                if revealed[x2][y2] == 'f': flags -= 1
                revealed[x2][y2] = True
                draw(x2, y2)

# checks board for win
def check_win():
    global game_over
    # return if flags not equal to mines
    if flags != mines: return
    # for each square
    for x in range(screen_x):
        for y in range(screen_y):
            # return if square unrevealed
            if revealed[x][y] == False: return
            # return if falsely marked mine
            elif revealed[x][y] == 'f' and board[x][y] != 'm': return
    # game over
    game_over = True
    # get elapsed time in seconds
    current_time = pygame.time.get_ticks()
    elapsed_ms = current_time - start_time
    elapsed_s = elapsed_ms // 1000
    # set win caption
    set_caption('Win! Time: ' + str(elapsed_s) + 's')

### main ###

# initialize time
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# game loop
while True:
    # tick
    clock.tick(60)
    # for each event
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            # quit game
            pygame.quit()
            sys.exit()
        # mouse event
        if event.type == pygame.MOUSEBUTTONUP:
            # if game over, continue
            if game_over: continue
            # if not correct button, continue
            if event.button != 1 and event.button != 3: continue
            # get clicked square
            pos = pygame.mouse.get_pos()
            x = pos[0] // grid
            y = pos[1] // grid
            # if already revealed, continue
            if revealed[x][y] == True: continue
            # left click
            if event.button == 1:
                # if revealing flag, decrement count
                if revealed[x][y] == 'f': flags -= 1
                revealed[x][y] = True
                # if mine
                if board[x][y] == 'm':
                    # game over
                    game_over = True
                    set_caption('Game over!')
                # if zero
                elif board[x][y] == 0:
                    # recursively reveal tile
                    recursive_reveal(x, y)
            # right click
            elif event.button == 3:
                # if not flagged
                if revealed[x][y] == False:
                    # flag tile
                    revealed[x][y] = 'f'
                    flags += 1
                # if flagged
                else:
                    # unflag tile
                    revealed[x][y] = False
                    flags -= 1
            # draw tile
            draw(x, y)
            # update display
            pygame.display.update()
            # if not game over
            if not game_over:
                # set caption to mine and flag count
                set_caption('Mines: ' + str(mines) + ' Flags: ' + str(flags))
            # check for win
            check_win()
