import pygame
from Utils.Components.Buttons import BasicButton
from Utils.Graphics import allignment


def draw(
    screen,
    screen_x,
    screen_y,
    WINDOWS_SIZE_X,
    WINDOWS_SIZE_Y,
    WINDOWS_COLOR,
    WINDOWS_POS_X,
    WINDOWS_POS_Y,
    img_x_icon,
    img_x_icon_x,
    img_x_icon_y,
    font,
    smallfont,
    footer,
    footer_text,
    EXIT_BTN_NAME,
):
    windows_bar = pygame.Surface((WINDOWS_SIZE_X, WINDOWS_SIZE_Y))
    windows_bar.fill(WINDOWS_COLOR)
    screen.blit(windows_bar, (WINDOWS_POS_X, WINDOWS_POS_Y))
    BasicButton.draw(
        screen=screen,
        BUTTON_X=img_x_icon_x,
        BUTTON_Y=img_x_icon_y,
        POS_X=allignment.relative_allign(
            LAYOUT_X=WINDOWS_POS_X,
            LAYOUT_Y=WINDOWS_POS_Y,
            LAYOUT_SCALE_X=WINDOWS_SIZE_X,
            LAYOUT_SCALE_Y=WINDOWS_SIZE_Y,
            location="X_RIGHT",
            component_x=img_x_icon_x,
            component_y=img_x_icon_y,
            MARGIN_LEVEL=80,
        ),
        POS_Y=allignment.relative_allign(
            LAYOUT_X=WINDOWS_POS_X,
            LAYOUT_Y=WINDOWS_POS_Y,
            LAYOUT_SCALE_X=WINDOWS_SIZE_X,
            LAYOUT_SCALE_Y=WINDOWS_SIZE_Y,
            location="Y_UP",
            component_x=img_x_icon_x,
            component_y=img_x_icon_y,
            MARGIN_LEVEL=80,
        ),
        font=font,
        text="",
        text_color=(0, 0, 0),
        button_color=(0, 0, 0),
        alpha=None,
        BTN_NAME=EXIT_BTN_NAME,
        IMAGE=img_x_icon,
    )

    if footer:
        footer_bar_y = WINDOWS_SIZE_Y / 100
        footer_bar = pygame.Surface((WINDOWS_SIZE_X, footer_bar_y))
        footer_bar.fill((255, 255, 255))
        screen.blit(
            footer_bar,
            (
                allignment.relative_allign(
                    LAYOUT_X=WINDOWS_POS_X,
                    LAYOUT_Y=WINDOWS_POS_Y,
                    LAYOUT_SCALE_X=WINDOWS_SIZE_X,
                    LAYOUT_SCALE_Y=WINDOWS_SIZE_Y,
                    location="X_CENTER",
                    component_x=WINDOWS_SIZE_X,
                    component_y=footer_bar_y,
                ),
                (
                    allignment.relative_allign(
                        LAYOUT_X=allignment.allign(
                            SCREEN_X=screen_x,
                            SCREEN_Y=screen_y,
                            location="X_CENTER",
                            image_x=WINDOWS_SIZE_X,
                            image_y=WINDOWS_SIZE_Y,
                        ),
                        LAYOUT_Y=allignment.allign(
                            SCREEN_X=screen_x,
                            SCREEN_Y=screen_y,
                            location="Y_CENTER",
                            image_x=WINDOWS_SIZE_X,
                            image_y=WINDOWS_SIZE_Y,
                        ),
                        LAYOUT_SCALE_X=WINDOWS_SIZE_X,
                        LAYOUT_SCALE_Y=WINDOWS_SIZE_Y,
                        location="Y_DOWN",
                        component_x=WINDOWS_SIZE_X,
                        component_y=footer_bar_y,
                        MARGIN_LEVEL=10,
                    )
                ),
            ),
        )

        footer_text = smallfont.render(footer_text, False, (255, 255, 255))
        screen.blit(
            footer_text,
            (
                allignment.relative_allign(
                    LAYOUT_X=WINDOWS_POS_X,
                    LAYOUT_Y=WINDOWS_POS_Y,
                    LAYOUT_SCALE_X=WINDOWS_SIZE_X,
                    LAYOUT_SCALE_Y=WINDOWS_SIZE_Y,
                    location="X_CENTER",
                    component_x=footer_text.get_width(),
                    component_y=footer_text.get_height(),
                ),
                (
                    allignment.relative_allign(
                        LAYOUT_X=WINDOWS_POS_X,
                        LAYOUT_Y=WINDOWS_POS_Y,
                        LAYOUT_SCALE_X=WINDOWS_SIZE_X,
                        LAYOUT_SCALE_Y=WINDOWS_SIZE_Y,
                        location="Y_DOWN",
                        component_x=footer_text.get_width(),
                        component_y=footer_text.get_height(),
                        MARGIN_LEVEL=30,
                    )
                ),
            ),
        )
