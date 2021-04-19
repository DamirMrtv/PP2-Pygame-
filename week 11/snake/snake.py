import pygame,sys
import random 
import time
import pickle

pygame.init()

WIDTH = 600
HEIGHT = 500

go = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Snake Game')
font = pygame.font.SysFont('Snap ITC', 20)
fonts = pygame.font.SysFont('Snap ITC',45)
music = pygame.mixer.Sound('Sound.ogg')
music.play(loops=-1)
FPS = 30
clock = pygame.time.Clock()

file_name = 'snake_saved.txt'

class Menu:
    def __init__(self, punkts = [120,140, u'Punkt',(250,250,30),(250,30,250),0]):
        self.punkts = punkts
    def render(self, screen, font,  num_punkt ):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    
    def menu(self):
        go = True
        font_menu = pygame.font.Font('Snap ITC.ttf',50)
        punkt = 0
        global level
        level = 0
        while go:
            screen.fill((186,224,232))
            ms = pygame.mouse.get_pos()
            for i in self.punkts:
                if ms[0]>i[0] and ms[0]<i[0]+155 and ms[1]>i[1] and ms[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -=1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt +=1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button ==1:
                    if punkt == 0:
                        go = False
                        level =1
                    elif punkt == 1:
                        go = False 
                        level = 2
                    elif punkt == 2:
                        go = False
                        level = 3
                    elif punkt == 3:
                        go = False
                        level = 4
                    elif punkt == 4:
                        sys.exit()
            
            screen.blit(screen, (0,0))
            pygame.display.flip()

class Snake:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (101,205,103), element, self.radius)

    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Snake2:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = 40
        self.dy = 35
        self.elements = [[250, 250], [270, 250], [290, 250]]
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (101,205,103), element, self.radius)

    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


class Food:

    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.image.load("apple.png")
        
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score):
    show = font.render('Score: ' + str(score), True, (101,205,103))
    screen.blit(show, (x, y-25))
    
def collision():
    if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1])):
        snake.is_add = True
        pygame.mixer.Sound('eat-apple.wav').play()
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)

def collision2():
    if(food.x in range(snake2.elements[0][0] - 20, snake2.elements[0][0])) and (food.y in range(snake2.elements[0][1] - 20, snake2.elements[0][1])):
        snake2.is_add = True
        pygame.mixer.Sound('eat-apple.wav').play()
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)

def is_in_walls():
    return snake.elements[0][0] > WIDTH - 25 or snake.elements[0][0] < 30 or snake.elements[0][1] > HEIGHT - 25 or snake.elements[0][1] < 30
    if level == 4:
        return snake2.elements[0][0] > WIDTH - 25 or snake2.elements[0][0] < 30 or snake2.elements[0][1] > HEIGHT - 25 or snake2.elements[0][1] < 30 or snake.elements[0][0] > WIDTH - 25 or snake.elements[0][0] < 30 or snake.elements[0][1] > HEIGHT - 25 or snake.elements[0][1] < 30

def game_over():
    screen.fill((219,255,222))
    txt = fonts.render('GAME OVER!', True, (245, 0, 0))
    my_score = fonts.render('Total score: ' + str(snake.score), True, (245, 0, 0))
    screen.blit(txt, (125, 150))
    screen.blit(my_score, (125, 250))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    
def show_walls():
    for i in range(0, WIDTH, 15):
        screen.blit(wall_image, (i,-15))
        screen.blit(wall_image, (i, HEIGHT - 10))
        screen.blit(wall_image, (-15, i))
        screen.blit(wall_image, (WIDTH - 10, i))
    if level == 2:
        for i in range(0, WIDTH, 50):
            screen.blit(wall_image, (i,1))
            screen.blit(wall_image, (i, HEIGHT + 50))
            screen.blit(wall_image, (1, i))
            screen.blit(wall_image, (WIDTH+50, i))
    if level == 3:
        for i in range(0, WIDTH , 30):
            screen.blit(wall_image, (i,0))
            screen.blit(wall_image, (i, HEIGHT - 25))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (WIDTH-25, i))


snake = Snake()
snake2 = Snake2()
food = Food()

punkts = [(120,140, u'Easy', (250,250,30), (250,30,250), 0),
          (120,210, u'Medium', (250,250,30), (250,30,250), 1),
          (120,280, u'Hard', (250,250,30), (250,30,250), 2),
          (120,340, u'Two players', (250,250,30), (250,30,250), 3),
          (120,400, u'Quit', (250,250,30), (250,30,250), 4)]

game =  Menu(punkts)
game.menu()

wall_image = pygame.image.load('wall.png')

def easy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 5
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -5
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -5
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 5

def snake2_wasd():
    for event in pygame.event.get():            
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                snake.dx = 10
                snake.dy = 0
            if event.key == pygame.K_a:
                snake.dx = -10
                snake.dy = 0
            if event.key == pygame.K_w:
                snake.dx = 0
                snake.dy = -10
            if event.key == pygame.K_s:
                snake.dx = 0
                snake.dy = 10
            if event.key == pygame.K_RIGHT:
                snake2.dx = 10
                snake2.dy = 0
            if event.key == pygame.K_LEFT:
                snake2.dx = -10
                snake2.dy = 0
            if event.key == pygame.K_UP:
                snake2.dx = 0
                snake2.dy = -10
            if event.key == pygame.K_DOWN:
                snake2.dx = 0
                snake2.dy = 10


def medium():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 10
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -10
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -10
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 10

def hard():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 15
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -15
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -15
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 15
    
while go:
    mil = clock.tick(FPS)
    if level == 1:
        easy()  
    elif level == 2:
        medium()
    elif level == 3:
        hard()
    elif level == 4:
        snake2.move()
        snake2.draw()
        snake2_wasd()
        collision2()
    
    if is_in_walls():
        game_over()
        go = False

        
    with open(file_name,'wb') as f:
        pickle.dump("total score:" +str(snake.score),f)
    
    collision()
    screen.fill((255,255,219))
    snake.move()
    snake.draw()
    food.draw()
    show_score(35, 45, snake.score)
    show_walls()
    pygame.display.flip()