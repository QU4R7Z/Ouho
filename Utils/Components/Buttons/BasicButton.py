import pygame
from Utils.Graphics import allignment
from Utils.Components.Buttons import ButtonZoneBuffer


def draw(
    screen,
    BUTTON_X,
    BUTTON_Y,
    POS_X,
    POS_Y,
    font,
    text,
    text_color,
    button_color,
    alpha,
    BTN_NAME,
    IMAGE,
):
    button_bar = pygame.Surface((BUTTON_X, BUTTON_Y))
    if alpha is not None:
        button_bar.set_alpha(alpha),
    button_bar.fill(button_color)
    screen.blit(button_bar, (POS_X, POS_Y))
    button_text = font.render(text, False, text_color)

    if IMAGE is not None:
        screen.blit(IMAGE, (POS_X, POS_Y))

    ButtonZoneBuffer.Buff(
        BTN_NAME=BTN_NAME,
        X1=POS_X,
        X2=POS_X + BUTTON_X,
        Y1=POS_Y,
        Y2=POS_Y + BUTTON_Y,
    )

    screen.blit(
        button_text,
        (
            allignment.relative_allign(
                LAYOUT_X=POS_X,
                LAYOUT_Y=POS_Y,
                LAYOUT_SCALE_X=BUTTON_X,
                LAYOUT_SCALE_Y=BUTTON_Y,
                location="X_CENTER",
                component_x=button_text.get_width(),
            ),
            allignment.relative_allign(
                LAYOUT_X=POS_X,
                LAYOUT_Y=POS_Y,
                LAYOUT_SCALE_X=BUTTON_X,
                LAYOUT_SCALE_Y=BUTTON_Y,
                location="Y_CENTER",
                component_y=button_text.get_height(),
            ),
        ),
    )
