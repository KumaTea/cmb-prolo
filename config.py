# ------ NOTE ------ #
#
# The coordinates here
# are based on Redmi K40,
# with the screen resolution
# of 1080x2400

center = 540  # 1080 / 2

cmb_left = 180
cmb_right = 900

cmb_first = 1850
cmb_second = 2000
cmb_third = 2150
cmb_fourth = 2300

cmb_nums = {
    '0': (center, cmb_fourth),
    '1': (cmb_left, cmb_first),
    '2': (center, cmb_first),
    '3': (cmb_right, cmb_first),
    '4': (cmb_left, cmb_second),
    '5': (center, cmb_second),
    '6': (cmb_right, cmb_second),
    '7': (cmb_left, cmb_third),
    '8': (center, cmb_third),
    '9': (cmb_right, cmb_third),
}

profit_coords = [300, 460, 780, 560]

lock_left = 240
lock_right = 840

lock_first = 1500
lock_second = 1685
lock_third = 1870
lock_fourth = 2065

lock_nums = {
    '0': (center, lock_fourth),
    '1': (lock_left, lock_first),
    '2': (center, lock_first),
    '3': (lock_right, lock_first),
    '4': (lock_left, lock_second),
    '5': (center, lock_second),
    '6': (lock_right, lock_second),
    '7': (lock_left, lock_third),
    '8': (center, lock_third),
    '9': (lock_right, lock_third),
}
