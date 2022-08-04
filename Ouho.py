import sys
import time

from pygame.locals import *
import os
from Utils import jsonreader
from Utils.Graphics import allignment
from Utils.Graphics.in_game import intro
from Utils.Components.Buttons import BasicButton

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
screen = pygame.display.set_mode((0, 0), DOUBLEBUF | HWSURFACE | FULLSCREEN)
screen_x, screen_y = screen.get_size()
print(screen_x, screen_y)
pygame.display.set_caption("Ouho")
clock = pygame.time.Clock()

# //////////////////////////////////////////////////////////////////////////////
# Images
img_quartz_flag_horizontal = pygame.image.load(
    load_file("Resources/quartz_flag_horizontal.png")
).convert_alpha()
img_quartz_flag_horizontal = pygame.transform.smoothscale(
    img_quartz_flag_horizontal,
    (
        screen_x * (img_quartz_flag_horizontal.get_width() / 3840),
        screen_y * (img_quartz_flag_horizontal.get_height() / 2160),
    ),
)
(
    img_quartz_flag_horizontal_x,
    img_quartz_flag_horizontal_y,
) = img_quartz_flag_horizontal.get_size()
img_quartz = pygame.image.load(load_file("Resources/quartz.png")).convert_alpha()
img_quartz = pygame.transform.smoothscale(
    img_quartz,
    (
        screen_x * (img_quartz.get_width() / 3840),
        screen_y * (img_quartz.get_height() / 2160),
    ),
)
img_quartz_x, img_quartz_y = img_quartz.get_size()
img_tiger_tank = pygame.image.load(
    load_file("Resources/tiger-tank.png")
).convert_alpha()
img_tiger_tank = pygame.transform.smoothscale(
    img_tiger_tank,
    (
        screen_x * (img_tiger_tank.get_width() / 3840),
        screen_y * (img_tiger_tank.get_height() / 2160),
    ),
)
img_tiger_tank_x, img_tiger_tank_y = img_tiger_tank.get_size()
img_ouho = pygame.image.load(load_file("Resources/ouho.png")).convert_alpha()
img_ouho = pygame.transform.smoothscale(
    img_ouho,
    (
        screen_x * (img_ouho.get_width() / 3840),
        screen_y * (img_ouho.get_height() / 2160),
    ),
)
img_ouho_x, img_ouho_y = img_ouho.get_size()
# Sound / Music
sound_intro = pygame.mixer.Sound(load_file("Resources/quartz_intro.wav"))

pygame.mixer.music.load(load_file("Resources/War_Music.wav"))

# Fonts

font_gmarket_regular = pygame.font.Font(
    load_file("Font/GmarketSansTTFMedium.ttf"), int(screen_y * (120 / 2160))
)
# //////////////////////////////////////////////////////////////////////////////
mainLoop = True
start_time = pygame.time.get_ticks()
intro_playsound, background_music = True, True
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

    if SI_TIME * 1 < pygame.time.get_ticks() < SI_TIME * 3:
        if intro_playsound:
            sound_intro.play()
            intro_playsound = False
        intro.draw_quartz(
            screen, screen_x, screen_y, img_quartz, img_quartz_x, img_quartz_y
        )
    if SI_TIME * 3.5 < pygame.time.get_ticks() < SI_TIME * 7.5:
        intro.supported(
            screen,
            screen_x,
            screen_y,
            font_gmarket_regular,
            img_quartz_flag_horizontal,
            img_quartz_flag_horizontal_x,
            img_quartz_flag_horizontal_y,
        )
    if SI_TIME * 7.5 < pygame.time.get_ticks():
        if background_music:
            pygame.mixer.music.play(-1)
            background_music = False
        screen.blit(img_tiger_tank, (0, 0))
        upbar = pygame.Surface((screen_x, img_ouho_x))
        upbar.set_alpha(80)
        upbar.fill((0, 0, 0))
        screen.blit(upbar, (0, 0))
        leftbar = pygame.Surface((img_ouho_x, screen_y))
        leftbar.set_alpha(80)
        leftbar.fill((0, 0, 0))
        screen.blit(leftbar, (0, 0))
        img_ouho.set_alpha(120)
        screen.blit(img_ouho, (0, 0))
        BasicButton.draw(
            screen,
            BUTTON_X=600,
            BUTTON_Y=100,
            POS_X=screen_x * (9 / 16),
            POS_Y=screen_y * (9 / 16),
            font=font_gmarket_regular,
            text="게임 시작",
            text_color=(255, 255, 255),
            button_color=(0, 0, 0),
            alpha=120,
        )

    pygame.display.flip()

# //////////////////////////////////////////////////////////////////////////////
pygame.quit()
sys.exit()
