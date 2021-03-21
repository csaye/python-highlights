import pygame, sys, random
from collections import deque

### globals ###

update = 10
score = 0
grid = 32
screen_x = 16; screen_y = 16
apple = False
take_input = True
paused = False

def game_quit():
    print("Final score: " + str(score))
    pygame.quit()
    sys.exit()

### screen ###

screen = pygame.display.set_mode((screen_x * grid, screen_y * grid))
pygame.display.set_caption('Score: 0')

### colors ###

white = (255, 255, 255)
black = (0, 0, 0)
red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)

### board ###

board = []
for y in range(0, screen_y):
    row = []
    for x in range(0, screen_x):
        row.append('')
    board.append(row)

def board_draw():
    screen.fill(black)
    
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            # get board tile
            tile = board[x][y]
            if tile == '': continue
            elif tile == 's': color = green
            elif tile == 'a': color = red
            # draw rect
            rect = ((x * grid, y * grid), (grid, grid))
            pygame.draw.rect(screen, color, rect)
            
    pygame.display.update()

def spawn_apple():
    global apple

    # get random position
    rand_x = random.randint(0, screen_x - 1)
    rand_y = random.randint(0, screen_y - 1)
    while (board[rand_x][rand_y] != ''):
        rand_x = random.randint(0, screen_x - 1)
        rand_y = random.randint(0, screen_y - 1)
    board[rand_x][rand_y] = 'a'
    apple = True

### snake ###

snake = deque([])
snake_x = 0; snake_y = 0
snake.append((snake_x, snake_y))

snake_dir = 'd'

def snake_switch(direction):
    global snake_dir, take_input
    
    # do not take opposite direction
    if (direction == 'u' and snake_dir != 'd'): snake_dir = 'u'; take_input = False
    elif (direction == 'l' and snake_dir != 'r'): snake_dir = 'l'; take_input = False
    elif (direction == 'd' and snake_dir != 'u'): snake_dir = 'd'; take_input = False
    elif (direction == 'r' and snake_dir != 'l'): snake_dir = 'r'; take_input = False

def snake_move():
    global snake_x, snake_y, score, apple
    
    next_x = snake_x; next_y = snake_y
    # move by direction
    if (snake_dir == 'u'): next_y -= 1
    if (snake_dir == 'l'): next_x -= 1
    if (snake_dir == 'd'): next_y += 1
    if (snake_dir == 'r'): next_x += 1
    # keep in bounds
    if (next_x < 0): next_x = screen_x - 1
    elif (next_x > screen_x - 1): next_x = 0
    if (next_y < 0): next_y = screen_y - 1
    elif (next_y > screen_y - 1): next_y = 0

    # update snake position
    snake_x = next_x; snake_y = next_y
    
    # if hit self, quit
    if (board[next_x][next_y] == 's'): game_quit()
    # if hit apple
    elif (board[next_x][next_y] == 'a'):
        board[next_x][next_y] = 's'
        snake.append((next_x, next_y))
        score += 1
        pygame.display.set_caption('Score: ' + str(score))
        apple = False
    # if empty, move
    else:
        board[next_x][next_y] = 's'
        snake.append((next_x, next_y))
        old = snake.popleft()
        board[old[0]][old[1]] = ''
    

### main ###

# time
clock = pygame.time.Clock()
frame = 0

# initialize board
board[snake_x][snake_y] = 's'
board_draw()

# loop
while True:

    # time
    clock.tick(60)
    if not paused: frame += 1

    # events
    for event in pygame.event.get():

        # quit
        if event.type == pygame.QUIT:
            game_quit()

        # keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: paused = not paused
            elif take_input:
                if event.key == pygame.K_w or event.key == pygame.K_UP: snake_switch('u')
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT: snake_switch('l')
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN: snake_switch('d')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: snake_switch('r')

    # update
    if ((not paused) and (frame % update == 0)):

        # move snake
        snake_move()

        # spawn apple
        if not apple: spawn_apple()
        
        # draw board
        board_draw()

        # reset input
        take_input = True
