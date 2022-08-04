from Utils.Graphics import allignment


def draw_quartz(screen, img_quartz, img_quartz_x, img_quartz_y):
    screen.blit(
        img_quartz,
        (
            allignment.allign("X_CENTER", image_x=img_quartz_x),
            allignment.allign("Y_CENTER", image_y=img_quartz_y),
        ),
    )


def supported(screen, font, img_quartz_flag_horizontal, img_quartz_flag_horizontal_x, img_quartz_flag_horizontal_y):
    screen.fill((1, 1, 1))
    supported_text = font.render("WITH", False, (255, 255, 255))
    screen.blit(supported_text, (allignment.allign("X_CENTER", image_x=supported_text.get_width()), 100))
    screen.blit(
        img_quartz_flag_horizontal,
        (
            allignment.allign("X_CENTER", image_x=img_quartz_flag_horizontal_x),
            allignment.allign("Y_CENTER", image_y=img_quartz_flag_horizontal_y),
        ),
    )
