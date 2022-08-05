BUTTON_NAME = []
ZONE_RANGE = []
DISABLED_BUTTON_NAME = []


def Buff(BTN_NAME, X1, X2, Y1, Y2):
    if BTN_NAME not in BUTTON_NAME:
        BUTTON_NAME.append(BTN_NAME)
        ZONE_RANGE.append([X1, X2, Y1, Y2])


def BUTTON_CLICKED(MOUSE_X, MOUSE_Y, MOUSE_CLICK):
    for i in range(len(ZONE_RANGE)):
        if (
            ZONE_RANGE[i][0] < MOUSE_X < ZONE_RANGE[i][1]
            and ZONE_RANGE[i][2] < MOUSE_Y < ZONE_RANGE[i][3]
            and MOUSE_CLICK
            and BUTTON_NAME[i] not in DISABLED_BUTTON_NAME
        ):
            print(BUTTON_NAME[i])
            return BUTTON_NAME[i]


def DISABLE_BUTTON(BTN_NAME):
    if BTN_NAME in BUTTON_NAME and BTN_NAME not in DISABLED_BUTTON_NAME:
        DISABLED_BUTTON_NAME.append(BTN_NAME)


def ABLE_BUTTON(BTN_NAME):
    if BTN_NAME in DISABLED_BUTTON_NAME:
        DISABLED_BUTTON_NAME.remove(BTN_NAME)
