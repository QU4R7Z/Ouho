import pygame

from Utils.Components.Buttons import BasicButton


def draw(
    screen,
    img_tiger_tank,
    screen_x,
    screen_y,
    img_ouho,
    img_ouho_x,
    img_ouho_y,
    font_gmarket_regular,
):
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
        BUTTON_X=screen_x * (6 / 16),
        BUTTON_Y=screen_y / 9,
        POS_X=screen_x * (9 / 16),
        POS_Y=screen_y * (5 / 16),
        font=font_gmarket_regular,
        text="혼자서 하기",
        text_color=(255, 255, 255),
        button_color=(0, 0, 0),
        alpha=120,
    )
    BasicButton.draw(
        screen,
        BUTTON_X=screen_x * (6 / 16),
        BUTTON_Y=screen_y / 9,
        POS_X=screen_x * (9 / 16),
        POS_Y=screen_y * (5 / 16) + screen_y / 9 + screen_y * 0.01,
        font=font_gmarket_regular,
        text="여럿이서 하기",
        text_color=(255, 255, 255),
        button_color=(0, 0, 0),
        alpha=120,
    )
    BasicButton.draw(
        screen,
        BUTTON_X=screen_x * (6 / 16),
        BUTTON_Y=screen_y / 9,
        POS_X=screen_x * (9 / 16),
        POS_Y=screen_y * (5 / 16) + 2 * (screen_y / 9 + screen_y * 0.01),
        font=font_gmarket_regular,
        text="설정",
        text_color=(255, 255, 255),
        button_color=(0, 0, 0),
        alpha=120,
    )
    BasicButton.draw(
        screen,
        BUTTON_X=screen_x * (6 / 16),
        BUTTON_Y=screen_y / 9,
        POS_X=screen_x * (9 / 16),
        POS_Y=screen_y * (5 / 16) + 3 * (screen_y / 9 + screen_y * 0.01),
        font=font_gmarket_regular,
        text="만든 사람들",
        text_color=(255, 255, 255),
        button_color=(0, 0, 0),
        alpha=120,
    )
    BasicButton.draw(
        screen,
        BUTTON_X=screen_x * (6 / 16),
        BUTTON_Y=screen_y / 9,
        POS_X=screen_x * (9 / 16),
        POS_Y=screen_y * (5 / 16) + 4 * (screen_y / 9 + screen_y * 0.01),
        font=font_gmarket_regular,
        text="종료",
        text_color=(255, 255, 255),
        button_color=(0, 0, 0),
        alpha=120,
    )
