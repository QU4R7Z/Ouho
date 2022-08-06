import pygame
from Utils.Components.Buttons import BasicButton

def draw(screen, screen_x, screen_y, WINDOWS_SIZE_X, WINDOWS_SIZE_Y, WINDOWS_COLOR, WINDOWS_POS_X, WINDOWS_POS_Y, img_x_icon,
    img_x_icon_x,
    img_x_icon_y):
    windows_bar = pygame.Surface((WINDOWS_SIZE_X, WINDOWS_SIZE_Y))
    windows_bar.fill(WINDOWS_COLOR)
    screen.blit(windows_bar, (WINDOWS_POS_X, WINDOWS_POS_Y))


