import sys
import time
import pygame
from pygame.locals import *
import os
from Utils import jsonreader
from Utils.Graphics.in_game import intro
from Utils import image_loader
from Utils.Graphics.in_game import game_main_ui
from Utils.Components.Buttons import ButtonZoneBuffer
from Utils.Graphics.in_game import creators_ui
from Utils.Graphics.in_game import settings_ui
import json


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
    (0, 0), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN
)
screen_x, screen_y = screen.get_size()
print(screen_x, screen_y)
pygame.display.set_caption("Ouho")
clock = pygame.time.Clock()

# //////////////////////////////////////////////////////////////////////////////
# Images
(
    img_quartz_flag_horizontal,
    img_quartz_flag_horizontal_x,
    img_quartz_flag_horizontal_y,
) = image_loader.load(
    path=load_file("Resources/quartz_flag_horizontal.png"),
    SCALE_X=screen_x * (5 / 16),
    SCALE_Y=screen_y * (111 / 300),
)
img_quartz, img_quartz_x, img_quartz_y = image_loader.load(
    path=load_file("Resources/quartz.png"),
    SCALE_X=screen_x * (416 / 1600),
    SCALE_Y=screen_y * (416 / 900),
)
img_tiger_tank, img_tiger_tank_x, img_tiger_tank_y = image_loader.load(
    path=load_file("Resources/tiger-tank.png"),
    SCALE_X=screen_x,
    SCALE_Y=screen_y,
)
img_ouho, img_ouho_x, img_ouho_y = image_loader.load(
    path=load_file("Resources/ouho.png"),
    SCALE_X=screen_x * (125 / 1600),
    SCALE_Y=screen_y * (125 / 900),
)
img_x_icon, img_x_icon_x, img_x_icon_y = image_loader.load(
    path=load_file("Resources/x_icon.png"), SCALE_X=screen_y / 20, SCALE_Y=screen_y / 20
)
# Sound / Music
sound_intro = pygame.mixer.Sound(load_file("Resources/quartz_intro.wav"))
pygame.mixer.music.load(load_file("Resources/War_Music.wav"))

# Fonts
font_gmarket_regular = pygame.font.Font(
    load_file("Font/GmarketSansTTFMedium.ttf"), int(screen_y * (120 / 2160))
)
font_gmarket_regular_small = pygame.font.Font(
    load_file("Font/GmarketSansTTFMedium.ttf"), int(screen_y * (60 / 2160))
)
# //////////////////////////////////////////////////////////////////////////////
mainLoop = True
start_time = pygame.time.get_ticks()
intro_playsound, background_music = True, True
SI_TIME = 1000
MOUSE_X, MOUSE_Y = -1, -1
MOUSE_CLICK = False
BUTTON_CLICKED_NAME = None
CREATORS_UI, SETTINGS_UI = False, False
LANGUAGE = "kr"
with open(
    load_file(f"Language/{str(LANGUAGE).lower()}.json"), encoding="utf8"
) as LANGUAGE_JSON:
    LANGUAGE = json.load(LANGUAGE_JSON)
while mainLoop:
    events = pygame.event.get()
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                MOUSE_CLICK = True
            if event.type == pygame.MOUSEWHEEL:
                pass
    BUTTON_CLICKED_NAME = ButtonZoneBuffer.BUTTON_CLICKED(
        MOUSE_X=MOUSE_X, MOUSE_Y=MOUSE_Y, MOUSE_CLICK=MOUSE_CLICK
    )
    dt = clock.tick(fps)

    # ////////////////////////////////////////////////////////////////////////////// INTRO
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
    # ////////////////////////////////////////////////////////////////////////////// MAIN
    if SI_TIME * 7.5 < pygame.time.get_ticks():
        if background_music:
            pygame.mixer.music.play(-1)
            background_music = False
        game_main_ui.draw(
            screen=screen,
            img_tiger_tank=img_tiger_tank,
            screen_x=screen_x,
            screen_y=screen_y,
            img_ouho=img_ouho,
            img_ouho_x=img_ouho_x,
            img_ouho_y=img_ouho_y,
            font=font_gmarket_regular,
            language=LANGUAGE,
        )

    # ////////////////////////////////////////////////////////////////////////////// CREATORS_UI
    if BUTTON_CLICKED_NAME == "BTN_CREATORS":
        CREATORS_UI = True
        ButtonZoneBuffer.ABLE_BUTTON("BTN_EXIT_CREATORS_UI")
    if CREATORS_UI:
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_SINGLEPLAY")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_MULTIPLAY")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_SETTINGS")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_CREATORS")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_EXIT")
        creators_ui.draw(
            screen=screen,
            screen_x=screen_x,
            screen_y=screen_y,
            font=font_gmarket_regular,
            smallfont=font_gmarket_regular_small,
            img_x_icon=img_x_icon,
            img_x_icon_x=img_x_icon_x,
            img_x_icon_y=img_x_icon_y,
            language=LANGUAGE,
            config=config,
        )
        if BUTTON_CLICKED_NAME == "BTN_EXIT_CREATORS_UI":
            ButtonZoneBuffer.ABLE_BUTTON("BTN_SINGLEPLAY")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_MULTIPLAY")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_SETTINGS")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_CREATORS")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_EXIT")
            ButtonZoneBuffer.DISABLE_BUTTON("BTN_EXIT_CREATORS_UI")
            CREATORS_UI = False

    # ////////////////////////////////////////////////////////////////////////////// SETTINGS_UI
    if BUTTON_CLICKED_NAME == "BTN_SETTINGS":
        SETTINGS_UI = True
        ButtonZoneBuffer.ABLE_BUTTON("BTN_EXIT_SETTINGS_UI")
    if SETTINGS_UI:
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_SINGLEPLAY")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_MULTIPLAY")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_SETTINGS")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_CREATORS")
        ButtonZoneBuffer.DISABLE_BUTTON("BTN_EXIT")
        settings_ui.draw(
            screen=screen,
            screen_x=screen_x,
            screen_y=screen_y,
            font=font_gmarket_regular,
            smallfont=font_gmarket_regular_small,
            img_x_icon=img_x_icon,
            img_x_icon_x=img_x_icon_x,
            img_x_icon_y=img_x_icon_y,
            language=LANGUAGE,
            config=config,
        )
        if BUTTON_CLICKED_NAME == "BTN_EXIT_SETTINGS_UI":
            ButtonZoneBuffer.ABLE_BUTTON("BTN_SINGLEPLAY")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_MULTIPLAY")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_SETTINGS")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_CREATORS")
            ButtonZoneBuffer.ABLE_BUTTON("BTN_EXIT")

            ButtonZoneBuffer.DISABLE_BUTTON("BTN_EXIT_SETTINGS_UI")
            SETTINGS_UI = False

    pygame.display.flip()
    MOUSE_CLICK = False

# //////////////////////////////////////////////////////////////////////////////
pygame.quit()
sys.exit()
