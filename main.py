import pygame
import random


WIDTH = 1000
HEIGHT = 1000
FPS = 3 #speed of the snake

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

GRID_NUMBERIDK = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()


class Food:
    def __init__(self, screen, head):
        self.position_x = 300
        self.position_y = 100
        self.width_x = GRID_NUMBERIDK
        self.width_y = GRID_NUMBERIDK
        self.head = head
        self.screen = screen
    def Draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.position_x, self.position_y, self.width_x, self.width_y))
    def CheckEaten(self):
        if self.head.position_x == self.position_x and self.head.position_y == self.position_y:
            self.head.Add_Tail()
            self.position_x = random.randrange(0, 1000, GRID_NUMBERIDK)
            self.position_y = random.randrange(0, 1000, GRID_NUMBERIDK)
            self.Draw()


class Tail:
     def __init__(self, screen):
        self.position_x = 0
        self.position_y = 0
        self.width_x = GRID_NUMBERIDK
        self.width_y = GRID_NUMBERIDK
        self.screen = screen
        self.tail = None
     def Move(self, position_x, position_y):
            old_x = self.position_x
            old_y = self.position_y
            self.position_x = position_x
            self.position_y = position_y
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.position_x, self.position_y, self.width_x, self.width_y))
            if self.tail:
                self.tail.Move(old_x, old_y)

     def Add_Tail(self):
         if self.tail:
             self.tail.Add_Tail()
         else:
             self.tail = Tail(self.screen)



class Head:
    def __init__(self, screen):
        self.position_x = 100
        self.position_y = 100
        self.width_x = GRID_NUMBERIDK
        self.width_y = GRID_NUMBERIDK
        self.screen = screen
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.tail = None
    def Move(self):
        if self.tail:
            self.tail.Move(self.position_x, self.position_y)
        self.direction = self.next_direction
        if self.direction == UP:
            self.position_y -= self.width_y
        elif self.direction == DOWN:
            self.position_y += self.width_y
        elif self.direction == RIGHT:
            self.position_x += self.width_x
        else:
            self.position_x -= self.width_x
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.position_x, self.position_y, self.width_x, self.width_y))
    def CheckSelfCollision(self):
        tail = self.tail
        while tail:
            if self.position_x == tail.position_x and self.position_y == tail.position_y:
                return True
            tail = tail.tail
        return False
    def Add_Tail(self):
        if self.tail:
            self.tail.Add_Tail()
        else:
            self.tail = Tail(self.screen)


head = Head(screen)
food = Food(screen, head)

running = True
food.Draw()
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and head.direction != DOWN: #ignore the fact they are reversed XDD
                head.next_direction = UP
            elif event.key == pygame.K_DOWN and head.direction != UP:
                head.next_direction = DOWN
            elif event.key == pygame.K_LEFT and head.direction != RIGHT:
                head.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and head.direction != LEFT:
                head.next_direction = RIGHT


    screen.fill(BLACK)


    head.Move()
    if head.CheckSelfCollision():
        running = False
    food.Draw()
    food.CheckEaten()


    pygame.display.flip()

pygame.quit()
