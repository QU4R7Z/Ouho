from Utils.Graphics import allignment


def draw_quartz(screen, SCREEN_X, SCREEN_Y, img_quartz, img_quartz_x, img_quartz_y):
    screen.blit(
        img_quartz,
        (
            allignment.allign(SCREEN_X, SCREEN_Y, "X_CENTER", image_x=img_quartz_x),
            allignment.allign(SCREEN_X, SCREEN_Y, "Y_CENTER", image_y=img_quartz_y),
        ),
    )


def supported(
    screen,
    SCREEN_X,
    SCREEN_Y,
    font,
    img_quartz_flag_horizontal,
    img_quartz_flag_horizontal_x,
    img_quartz_flag_horizontal_y,
):
    screen.fill((1, 1, 1))
    supported_text = font.render("WITH", False, (255, 255, 255))
    screen.blit(
        supported_text,
        (
            allignment.allign(
                SCREEN_X, SCREEN_Y, "X_CENTER", image_x=supported_text.get_width()
            ),
            SCREEN_Y * (60 / 2160),
        ),
    )
    screen.blit(
        img_quartz_flag_horizontal,
        (
            allignment.allign(
                SCREEN_X, SCREEN_Y, "X_CENTER", image_x=img_quartz_flag_horizontal_x
            ),
            allignment.allign(
                SCREEN_X, SCREEN_Y, "Y_CENTER", image_y=img_quartz_flag_horizontal_y
            ),
        ),
    )
