import pygame, sys, math, random

### globals ###

threshold = 0.5
update = 10
paused = False

black = (0, 0, 0)
white = (255, 255, 255)

### screen ###

grid = 16
screen_x = 32; screen_y = 32
screen = pygame.display.set_mode((screen_x * grid, screen_y * grid))
pygame.display.set_caption('Conway')

### board ###

board = []
for y in range(0, screen_y):
    row = []
    for x in range(0, screen_x):
        if random.random() > threshold: row.append(1)
        else: row.append(0)
    board.append(row)

def score(x, y):
    score = 0
    l_x = x - 1; r_x = x + 1
    u_y = y - 1; d_y = y + 1
    if (l_x < 0): l_x = screen_x - 1
    if (r_x > screen_x - 1): r_x = 0
    if (u_y < 0): u_y = screen_y - 1
    if (d_y > screen_y - 1): d_y = 0
    adj = ((l_x, y),(l_x, u_y),(x, u_y),(r_x, u_y),(r_x, y),(r_x, d_y),(x, d_y),(l_x, d_y))
    for a in adj:
        tile = board[a[0]][a[1]]
        if (tile == 1 or tile == '-'): score += 1
    return score

def simulate():
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            s = score(x, y)
            tile = board[x][y]
            if tile == 1:
                if s < 2 or s > 3:
                    board[x][y] = '-'
            elif tile == 0:
                if s == 3:
                    board[x][y] = '+'

def draw():
    screen.fill(black)
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            if board[x][y] == '+': board[x][y] = 1
            elif board[x][y] == '-': board[x][y] = 0
            if board[x][y] == 1:
                rect = ((x * grid, y * grid), (grid, grid))
                pygame.draw.rect(screen, white, rect)
    pygame.display.update()

### main ###

clock = pygame.time.Clock()
frame = 0
draw()

while True:
    clock.tick(60)
    if not paused: frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos_x = math.floor(pos[0] / grid)
            pos_y = math.floor(pos[1] / grid)
            tile = board[pos_x][pos_y]
            if tile == 0: board[pos_x][pos_y] = 1
            elif tile == 1: board[pos_x][pos_y] = 0
            draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: paused = not paused

    if not paused and frame % update == 0:
        simulate()
        draw()
