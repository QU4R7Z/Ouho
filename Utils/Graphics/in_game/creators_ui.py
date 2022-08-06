import pygame
from Utils.Graphics import allignment
from Utils.Components.Buttons import BasicButton


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
):
    BAR_SIZE_X = screen_x / 3
    BAR_SIZE_Y = screen_y / 1.5
    creator_bar = pygame.Surface((BAR_SIZE_X, BAR_SIZE_Y))
    creator_bar.fill((0, 0, 0))
    screen.blit(
        creator_bar,
        (
            allignment.allign(
                SCREEN_X=screen_x,
                SCREEN_Y=screen_y,
                location="X_CENTER",
                image_x=BAR_SIZE_X,
                image_y=BAR_SIZE_Y,
            ),
            allignment.allign(
                SCREEN_X=screen_x,
                SCREEN_Y=screen_y,
                location="Y_CENTER",
                image_x=BAR_SIZE_X,
                image_y=BAR_SIZE_Y,
            ),
        ),
    )

    BasicButton.draw(
        screen=screen,
        BUTTON_X=img_x_icon_x,
        BUTTON_Y=img_x_icon_y,
        POS_X=allignment.relative_allign(
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
            location="X_RIGHT",
            component_x=img_x_icon_x,
            component_y=img_x_icon_y,
            MARGIN_LEVEL=80,
        ),
        POS_Y=allignment.relative_allign(
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
            component_x=img_x_icon_x,
            component_y=img_x_icon_y,
            MARGIN_LEVEL=80,
        ),
        font=font,
        text="",
        text_color=(0, 0, 0),
        button_color=(0, 0, 0),
        alpha=None,
        BTN_NAME="BTN_EXIT_CREATORS_UI",
        IMAGE=img_x_icon,
    )

    shi3do_text = font.render(language["SHI3DO"], False, (255, 255, 255))
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

    footer_bar_y = screen_y / 500
    footer_bar = pygame.Surface((BAR_SIZE_X, footer_bar_y))
    footer_bar.fill((255, 255, 255))
    screen.blit(
        footer_bar,
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
                component_x=BAR_SIZE_X,
                component_y=footer_bar_y,
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
                    location="Y_DOWN",
                    component_x=BAR_SIZE_X,
                    component_y=footer_bar_y,
                    MARGIN_LEVEL=10,
                )
            ),
        ),
    )

    QU4R7Z_text = smallfont.render("QU4R7Z", False, (255, 255, 255))
    screen.blit(
        QU4R7Z_text,
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
                component_x=QU4R7Z_text.get_width(),
                component_y=QU4R7Z_text.get_height(),
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
                    location="Y_DOWN",
                    component_x=QU4R7Z_text.get_width(),
                    component_y=QU4R7Z_text.get_height(),
                    MARGIN_LEVEL=30,
                )
            ),
        ),
    )
