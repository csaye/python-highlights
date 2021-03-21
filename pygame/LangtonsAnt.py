import pygame, sys, math, random

### globals ###

update = 10
sims = 1
paused = False

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

### screen ###

def caption():
    pygame.display.set_caption('Lanton\'s Ant | Iteration ' + str(itr))

itr = 0
grid = 8
screen_x = 64; screen_y = 64
screen = pygame.display.set_mode((screen_x * grid, screen_y * grid))
caption()

### board ###

board = []
for y in range(0, screen_y):
    row = []
    for x in range(0, screen_x):
        row.append(0)
    board.append(row)

ant_x = math.floor(screen_x / 2)
ant_y = math.floor(screen_y / 2)
dirc = "l"

def move():
    global dirc, ant_x, ant_y
    
    if dirc == "l": ant_x -= 1
    elif dirc == "r": ant_x += 1
    elif dirc == "u": ant_y -= 1
    elif dirc == "d": ant_y += 1

def turn(t):
    global dirc
    
    if t == "cw":
        if dirc == "l": dirc = "u"
        elif dirc == "u": dirc = "r"
        elif dirc == "r": dirc = "d"
        elif dirc == "d": dirc = "l"
    elif t == "cc":
        if dirc == "l": dirc = "d"
        elif dirc == "d": dirc = "r"
        elif dirc == "r": dirc = "u"
        elif dirc == "u": dirc = "l"

def simulate():
    if board[ant_x][ant_y] == 0:
        board[ant_x][ant_y] = 1
        turn("cw")
    else:
        board[ant_x][ant_y] = 0
        turn("cc")
    move()

def draw():
    screen.fill(white)
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            if x == ant_x and y == ant_y:
                rect = ((x * grid, y * grid), (grid, grid))
                pygame.draw.rect(screen, red, rect)
            elif board[x][y] == 1:
                rect = ((x * grid, y * grid), (grid, grid))
                pygame.draw.rect(screen, black, rect)
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: paused = not paused
            elif event.key == pygame.K_UP:
                update += 1
                print("Update at " + str(update))
            elif event.key == pygame.K_DOWN:
                if update > 1: update -= 1
                print("Update at " + str(update))
            elif event.key == pygame.K_RIGHT:
                sims += 1
                print("Simulations at " + str(sims))
            elif event.key == pygame.K_LEFT:
                if sims > 1: sims -= 1
                print("Simulations at " + str(sims))

    if not paused and frame % update == 0:

        for i in range(0, sims):
            itr += 1
            simulate()
            
        draw()
        caption()
