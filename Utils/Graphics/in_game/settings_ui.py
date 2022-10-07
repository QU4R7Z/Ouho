import pygame
from Utils.Graphics import allignment
from Utils.Components.Windows import BasicWindow


def draw(
    screen,
    screen_x,
    screen_y,
    font,
    smallfont,
    img_x_icon,
    img_x_icon_x,
    img_x_icon_y,
    language,
    config,
):
    BAR_SIZE_X = screen_x / 3
    BAR_SIZE_Y = screen_y / 1.5
    BasicWindow.draw(
        screen=screen,
        screen_x=screen_x,
        screen_y=screen_y,
        WINDOWS_SIZE_X=BAR_SIZE_X,
        WINDOWS_SIZE_Y=BAR_SIZE_Y,
        WINDOWS_COLOR=(0, 0, 0),
        WINDOWS_POS_X=allignment.allign(
            SCREEN_X=screen_x,
            SCREEN_Y=screen_y,
            location="X_CENTER",
            image_x=BAR_SIZE_X,
            image_y=BAR_SIZE_Y,
        ),
        WINDOWS_POS_Y=allignment.allign(
            SCREEN_X=screen_x,
            SCREEN_Y=screen_y,
            location="Y_CENTER",
            image_x=BAR_SIZE_X,
            image_y=BAR_SIZE_Y,
        ),
        img_x_icon=img_x_icon,
        img_x_icon_x=img_x_icon_x,
        img_x_icon_y=img_x_icon_y,
        font=font,
        smallfont=smallfont,
        footer=True,
        footer_text=f"v{config.version}",
        EXIT_BTN_NAME="BTN_EXIT_SETTINGS_UI",
    )

    shi3do_text = font.render(language["SETTINGS"], False, (255, 255, 255))
    screen.blit(
        shi3do_text,
        (
            allignment.relative_allign(
                LAYOUT_X=allignment.allign(
                    SCREEN_X=screen_x,
                    SCREEN_Y=screen_y,
                    location="X_CENTER",
                    image_x=BAR_SIZE_X,
                    image_y=BAR_SIZE_Y,
                ),
                LAYOUT_Y=allignment.allign(
                    SCREEN_X=screen_x,
                    SCREEN_Y=screen_y,
                    location="Y_CENTER",
                    image_x=BAR_SIZE_X,
                    image_y=BAR_SIZE_Y,
                ),
                LAYOUT_SCALE_X=BAR_SIZE_X,
                LAYOUT_SCALE_Y=BAR_SIZE_Y,
                location="X_CENTER",
                component_x=shi3do_text.get_width(),
                component_y=shi3do_text.get_height(),
            ),
            (
                allignment.relative_allign(
                    LAYOUT_X=allignment.allign(
                        SCREEN_X=screen_x,
                        SCREEN_Y=screen_y,
                        location="X_CENTER",
                        image_x=BAR_SIZE_X,
                        image_y=BAR_SIZE_Y,
                    ),
                    LAYOUT_Y=allignment.allign(
                        SCREEN_X=screen_x,
                        SCREEN_Y=screen_y,
                        location="Y_CENTER",
                        image_x=BAR_SIZE_X,
                        image_y=BAR_SIZE_Y,
                    ),
                    LAYOUT_SCALE_X=BAR_SIZE_X,
                    LAYOUT_SCALE_Y=BAR_SIZE_Y,
                    location="Y_UP",
                    component_x=shi3do_text.get_width(),
                    component_y=shi3do_text.get_height(),
                    MARGIN_LEVEL=20,
                )
            ),
        ),
    )
