SCREEN_X = 3840
SCREEN_Y = 2160
def allign(location="X_CENTER", image_x=0, image_y=0):
    try:
        if location == 'X_CENTER':
            return (SCREEN_X - image_x) / 2
        if location == 'Y_CENTER':
            return (SCREEN_Y - image_y) / 2
    except Exception as e:
        print(e)
        return None
