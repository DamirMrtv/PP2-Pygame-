import pygame


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,100,10)
YELLOW = (255,255,0)
LIME = (180,255,100)
PURPLE = (240, 0, 255)
SKYBLUE = (0,255,255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


def erase(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x, y), 40)

flowItem = 0
Itemcount = 4

current_color = 0
colors = (RED,BLUE,WHITE,GREEN,ORANGE,YELLOW,LIME,PURPLE,SKYBLUE)
current_size = 0
size = (10,50,100,150,200)
game_over = False

prev, cur = None, None
screen.fill(BLACK)

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_z:
            flowItem = (flowItem + 1 ) % Itemcount
        elif event.key == pygame.K_x:
            current_color = (current_color + 1) % len(colors)
        elif event.key == pygame.K_SPACE:
            current_size = (current_size + 1) % len(size)
    if event.type == pygame.QUIT:
        game_over = True
        pygame.image.save(screen, 'screen.jpg')
    if event.type == pygame.MOUSEBUTTONDOWN:
      prev = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEMOTION:
      cur = pygame.mouse.get_pos()
      if prev and flowItem == 0:
        pygame.draw.line(screen, colors[current_color], prev, cur, 1)
        prev = cur
      if prev and flowItem == 1:
          pygame.draw.circle(screen, colors[current_color], prev, size[current_size])
      if prev and flowItem == 2:
          pygame.draw.rect(screen, colors[current_color], (cur[0],cur[1],size[current_size],size[current_size]))
    if event.type == pygame.MOUSEBUTTONUP:
      prev = None
    
    
    elif flowItem == 3:
        erase(screen, *cur )

  pygame.display.flip()

  clock.tick(30)


pygame.quit()