import pygame, sys, random
pygame.init()

### globals ###

size = 4
grid = 128
scrambles = size * size * 8
slides = 0

black = (0, 0, 0)

directions = ['up', 'right', 'down', 'left']

roboto = pygame.font.SysFont('Roboto', int(grid / 2))

### screen ###

screen_size = (size * grid, size * grid)
screen = pygame.display.set_mode(screen_size)

def update_caption():
    pygame.display.set_caption('Slides: ' + str(slides))

update_caption()

### board ###

# checks for win
def check_win():
    global board
    for y in range(size):
        for x in range(size):
            val = x + size * y
            if board[x][y] != val: return
    pygame.display.set_caption('Win')

# slides board in given direction
def slide(direction, scrambling):
    global slides
    for x in range(size):
        for y in range(size):
            if board[x][y] == 0:
                
                if direction == 'up':
                    if y == size - 1: return
                    board[x][y] = board[x][y + 1]
                    board[x][y + 1] = 0
                elif direction == 'right':
                    if x == 0: return
                    board[x][y] = board[x - 1][y]
                    board[x - 1][y] = 0
                elif direction == 'down':
                    if y == 0: return
                    board[x][y] = board[x][y - 1]
                    board[x][y - 1] = 0
                elif direction == 'left':
                    if x == size - 1: return
                    board[x][y] = board[x + 1][y]
                    board[x + 1][y] = 0

                if not scrambling:
                    slides += 1
                    update_caption()
                    check_win()
                    draw_board()
                    
                return

# initialize board
board = []
for y in range(size):
    row = []
    for x in range(size):
        row.append((size * x) + y)
    board.append(row)

# draws board
def draw_board():
    screen.fill(black)
    for y in range(size):
        for x in range(size):
            if board[x][y] > 0:
                # draw rect
                rect = ((x * grid, y * grid), (grid, grid))
                val = int((board[x][y] / (size * size)) * 255)
                color = (val, val, 255)
                pygame.draw.rect(screen, color, rect)
                # blit text
                num = board[x][y]
                text_surface = roboto.render(str(num), False, black)
                text_pos = (x * grid, y * grid)
                screen.blit(text_surface, text_pos)
    pygame.display.update()

# scramble board
for i in range(scrambles):
    direction = random.choice(directions)
    slide(direction, True)

### main ###

clock = pygame.time.Clock()
frame = 0

draw_board()
while True:

    clock.tick(60)
    frame += 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: slide('up', False)
            elif event.key == pygame.K_RIGHT: slide('right', False)
            elif event.key == pygame.K_DOWN: slide('down', False)
            elif event.key == pygame.K_LEFT: slide('left', False)
