import pygame

#define class flappyBird
class FlappyBird:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.velocity = 0
        self.gravity = 1

#updates the position of the bird based on its velocity and gravity
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

#hanges the velocity of the bird when the space key is pressed
    def flap(self):
        self.velocity = -5

bird = FlappyBird()

pygame.init()

screen = pygame.display.set_mode((400, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (bird.x, bird.y), 20)

    bird.update()

    pygame.display.update()

pygame.quit()
