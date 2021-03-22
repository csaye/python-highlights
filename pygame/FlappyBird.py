### imports ###

import pygame, sys, random

### globals ###

update = 12
grid = 16
screen_x = 32; screen_y = 16
score = 0
pipe_interval = 8

green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

### screen ###

def update_caption():
    caption = 'Score: ' + str(score)
    pygame.display.set_caption(caption)

screen_size = (screen_x * grid, screen_y * grid)
screen = pygame.display.set_mode(screen_size)
update_caption()

### board ###

board = []
for x in range(screen_x):
    row = []
    for y in range(screen_y):
        row.append('')
    board.append(row)

def draw_board():
    screen.fill(blue)
    for y in range(screen_y):
        for x in range(screen_x):
            if board[x][y] == '': continue
            elif board[x][y] == 'player': color = yellow
            elif board[x][y] == 'pipe': color = green
            rect = ((x * grid, y * grid), (grid, grid))
            pygame.draw.rect(screen, color, rect)
    pygame.display.update()

def spawn_pipe():
    hole_size = random.randint(3, 5)
    hole_pos = random.randint(0, screen_y - hole_size)
    hole = []
    for y in range(hole_pos, hole_pos + hole_size):
        hole.append(y)
    for y in range(screen_y):
        if y in hole: continue
        board[screen_x - 1][y] = 'pipe'

def move_pipes():
    global score, board
    for x in range(screen_x):
        increment_score = False
        for y in range(screen_y):
            if board[x][y] == 'pipe':
                board[x][y] = ''
                if x > 0:
                    board[x - 1][y] = 'pipe'
                    if x - 1 == player_x:
                        increment_score = True
                        if y == player_y:
                            game_over()
        if increment_score: score += 1

### player ###

flapping = False

player_x = screen_x // 4
player_y = screen_y // 2
board[player_x][player_y] = 'player'

def move_player():
    global flapping, player_x, player_y
    board[player_x][player_y] = ''
    if flapping: player_y -= 1
    else: player_y += 1
    if player_y < 0 or player_y > screen_y - 1: game_over()
    board[player_x][player_y] = 'player'

### main ###

def game_over():
    print('Game over')
    print('Your score was ' + str(score))
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()
frame = 0

draw_board()
while True:
    
    clock.tick(60)
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            k = event.key
            if k == pygame.K_w or k == pygame.K_UP: flapping = True

    if frame % update == 0:
        move_player()
        move_pipes()
        if frame % (update * pipe_interval) == 0:
            spawn_pipe()
        update_caption()
        draw_board()
        flapping = False
