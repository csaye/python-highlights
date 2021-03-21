import pygame, sys, math

### globals ###

update = 10
paused = True
done = False
cur_y = 0

black = (0, 0, 0)
white = (255, 255, 255)
blue = (200, 200, 255)

def quit_game():
    pygame.quit()
    sys.exit()

### screen ###

grid = 8
screen_x = 64; screen_y = 64
screen = pygame.display.set_mode((screen_x * grid, screen_y * grid))
pygame.display.set_caption('Rule 110')
screen.fill(white)
pygame.display.update()

### rows ###

# initialize
last_row = []
cur_row = []
for x in range(0, screen_x):
    last_row.append(0)
    cur_row.append(0)

def simulate():
    global cur_y
    if cur_y > screen_y - 1: return
    for x in range(0, screen_x - 2):
        a = last_row[x]
        b = last_row[x + 1]
        c = last_row[x + 2]
        # not 111 or 100/000
        if (not (a and b and c)) and (b or c):
            cur_row[x + 1] = 1

def draw():
    for x in range(0, screen_x):
        rect = ((x * grid, cur_y * grid), (grid, grid))
        if cur_row[x] == 1: color = black
        else: color = blue
        pygame.draw.rect(screen, color, rect)
    pygame.display.update()

def mouse_click():
    pos = pygame.mouse.get_pos()
    pos_x = math.floor(pos[0] / grid)
    pos_y = math.floor(pos[1] / grid)
    # if current row
    if (pos_y == cur_y):
        if cur_row[pos_x] == 0: cur_row[pos_x] = 1
        else: cur_row[pos_x] = 0
        draw()
        

### main ###

clock = pygame.time.Clock()
frame = 0
draw()

while True:
    clock.tick(60)
    if not paused: frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.MOUSEBUTTONUP and not done:
            mouse_click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not done:
                paused = not paused
            elif event.key == pygame.K_ESCAPE:
                quit_game()

    if not paused and frame % update == 0:
        # increment current row
        if cur_y < screen_y - 1:
            last_row = cur_row.copy()
            for i in range(0, screen_x): cur_row[i] = 0
            cur_y += 1
        else:
            paused = True
            done = True
        # simulate and draw
        simulate()
        draw()
        
