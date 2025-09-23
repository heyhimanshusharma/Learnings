import pygame, sys

# Some general setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
screen = pygame.display.set_mode((800,800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    clock.tick()