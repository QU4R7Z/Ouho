import sys
import time

from pygame.locals import *
import os
from Utils import jsonreader
from Utils.Graphics import allignment
from Utils.Graphics.in_game import intro

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
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
screen = pygame.display.set_mode(
    (3840, 2160), DOUBLEBUF | HWSURFACE | SCALED | FULLSCREEN
)
screen_x, screen_y = screen.get_size()
print(screen_x, screen_y)
pygame.display.set_caption("Ouho")
clock = pygame.time.Clock()

# //////////////////////////////////////////////////////////////////////////////
# Images
img_quartz_flag_horizontal = pygame.image.load(
    load_file("Resources/quartz_flag_horizontal.png")
).convert_alpha()
(
    img_quartz_flag_horizontal_x,
    img_quartz_flag_horizontal_y,
) = img_quartz_flag_horizontal.get_size()
img_quartz = pygame.image.load(load_file("Resources/quartz.png")).convert_alpha()
img_quartz_x, img_quartz_y = img_quartz.get_size()

# Sound / Music
sound_intro = pygame.mixer.Sound(load_file("Resources/quartz_intro.wav"))

# Fonts
font_gmarket_regular = pygame.font.Font(load_file("Font/GmarketSansTTFMedium.ttf"), 120)
# //////////////////////////////////////////////////////////////////////////////
mainLoop = True
start_time = pygame.time.get_ticks()
intro_playsound = True
SI_TIME = 1000
while mainLoop:
    events = pygame.event.get()
    screen.fill((0, 0, 0))
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

    if SI_TIME * 1 < pygame.time.get_ticks() - start_time < SI_TIME * 3:
        if intro_playsound:
            sound_intro.play()
            intro_playsound = False
        intro.draw_quartz(screen, img_quartz, img_quartz_x, img_quartz_y)
    if SI_TIME * 4 < pygame.time.get_ticks() - start_time < SI_TIME * 8:
        intro.supported(
            screen,
            font_gmarket_regular,
            img_quartz_flag_horizontal,
            img_quartz_flag_horizontal_x,
            img_quartz_flag_horizontal_y,
        )
    
    pygame.display.flip()

# //////////////////////////////////////////////////////////////////////////////
pygame.quit()
sys.exit()
