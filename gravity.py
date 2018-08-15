import pygame
 
 
pygame.init()
 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)
pink = (255,114,187)
 
display_width = 800
display_height = 600
FPS = 60
 
gameDisplay = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption('G R A V I T Y')
gameExit = False
 
clock = pygame.time.Clock()
 
class Ball:
    GRAVITY = 0.2
    def __init__ (self, screen, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.yVel = 0
 
    def draw(self):
        if self.y + self.size > display_height:
            self.yVel = -self.yVel * 0.8
        #if self.y + self.size == display_height:
        #   self.yVel = self.y
        self.yVel = self.yVel + self.GRAVITY
        self.y = int(self.y + self.yVel)
        pygame.draw.circle(self.screen, red,[self.x,self.y], self.size)
 
class Rectangle:
    GRAVITY = 0.2
    def __init__ (self, screen, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.yVel = 0
    def draw(self):
        if self.y + self.size >= display_height:
            self.yVel = 0
            self.y = display_height - self.size
        self.yVel = self.yVel + self.GRAVITY
        self.y = int(self.y + self.yVel)
        pygame.draw.rect(self.screen, blue,[self.x,self.y,self.size,self.size])
 
 
player1 = None
player2 = None
while not gameExit:
    gameDisplay.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            x,y = pygame.mouse.get_pos()
            print("x:{}, y:{}".format(x, y))
            player1 = Ball(gameDisplay,x,y,20)
        elif buttons[2]:
            x,y = pygame.mouse.get_pos()
            player2 = Rectangle(gameDisplay,x,y,20)
    if player1:
        player1.draw()
    if player2:
        player2.draw()
 
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()