import sys

from pygame.locals import *
import os
from Utils import jsonreader

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame


# //////////////////////////////////////////////////////////////////////////////
def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


# //////////////////////////////////////////////////////////////////////////////
config = jsonreader.get(load_file("Config/config.json"))
fps = int(config.fps)
pygame.init()
icon = pygame.image.load(load_file("Icon/OUHO.png"))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1920, 1080), DOUBLEBUF | HWSURFACE | SCALED | FULLSCREEN)
screen_x, screen_y = screen.get_size()
print(screen_x, screen_y)
pygame.display.set_caption("Ouho")
clock = pygame.time.Clock()

# //////////////////////////////////////////////////////////////////////////////
mainLoop = True
while mainLoop:
    events = pygame.event.get()
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEWHEEL:
                pass

    dt = clock.tick(fps)

    screen.fill((0, 0, 0))
    pygame.display.flip()

# //////////////////////////////////////////////////////////////////////////////
pygame.quit()
sys.exit()
