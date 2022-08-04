def allign(SCREEN_X, SCREEN_Y, location="X_CENTER", image_x=0, image_y=0):
    try:
        if location == "X_CENTER":
            return (SCREEN_X - image_x) / 2
        if location == "Y_CENTER":
            return (SCREEN_Y - image_y) / 2

    except Exception as e:
        print(e)
        return None


def relative_allign(
    LAYOUT_X,
    LAYOUT_Y,
    LAYOUT_SCALE_X,
    LAYOUT_SCALE_Y,
    location="X_CENTER",
    component_x=0,
    component_y=0,
):
    try:
        if location == "X_CENTER":
            return LAYOUT_X + (LAYOUT_SCALE_X - component_x) / 2
        if location == "Y_CENTER":
            return LAYOUT_Y + (LAYOUT_SCALE_Y - component_y) / 2
    except Exception as e:
        print(e)
        return None
