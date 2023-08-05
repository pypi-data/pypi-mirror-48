from skimage import color


def trapezoid_fuzzy_color_segmentation(image):
    rgb_image = image.copy()
    hsv_image = color.rgb2hsv(rgb_image)

    h_channel = 360 * hsv_image[:, :, 0]

    for i in range(h_channel.shape[0]):
        for j in range(h_channel.shape[1]):

            p_red = fuzzy_segmentation_red_trapezoid(h_channel[i, j])
            p_orange = fuzzy_segmentation_orange_trapezoid(h_channel[i, j])
            p_yellow = fuzzy_segmentation_yellow_trapezoid(h_channel[i, j])
            p_green = fuzzy_segmentation_green_trapezoid(h_channel[i, j])
            p_cyan = fuzzy_segmentation_cyan_trapezoid(h_channel[i, j])
            p_blue = fuzzy_segmentation_blue_trapezoid(h_channel[i, j])
            p_purple = fuzzy_segmentation_purple_trapezoid(h_channel[i, j])

            m = max([p_red, p_orange, p_yellow, p_green, p_cyan, p_blue, p_purple])

            if m == p_red:
                rgb_image[i, j, 0] = 255
                rgb_image[i, j, 1] = 0
                rgb_image[i, j, 2] = 0
            elif m == p_orange:
                rgb_image[i, j, 0] = 255
                rgb_image[i, j, 1] = 165
                rgb_image[i, j, 2] = 0
            elif m == p_yellow:
                rgb_image[i, j, 0] = 255
                rgb_image[i, j, 1] = 255
                rgb_image[i, j, 2] = 0
            elif m == p_green:
                rgb_image[i, j, 0] = 0
                rgb_image[i, j, 1] = 128
                rgb_image[i, j, 2] = 0
            elif m == p_cyan:
                rgb_image[i, j, 0] = 0
                rgb_image[i, j, 1] = 255
                rgb_image[i, j, 2] = 255
            elif m == p_blue:
                rgb_image[i, j, 0] = 0
                rgb_image[i, j, 1] = 0
                rgb_image[i, j, 2] = 255
            elif m == p_purple:
                rgb_image[i, j, 0] = 128
                rgb_image[i, j, 1] = 0
                rgb_image[i, j, 2] = 128

    return rgb_image


def fuzzy_segmentation_red_trapezoid(h):
    if (0 <= h <= 10) or (330 < h <= 360):
        return (1)
    elif 10 < h <= 20:
        return -0.1 * h + 2
    elif 20 < h <= 300:
        return 0
    elif 300 < h <= 330:
        return (1 / 30) * h - 10


def fuzzy_segmentation_orange_trapezoid(h):
    if 0 <= h <= 10 or 55 < h <= 360:
        return 0
    elif 10 < h <= 20:
        return 0.1 * h - 1
    elif 20 < h <= 40:
        return 1
    elif 40 < h <= 55:
        return (-1 / 15) * h + 11 / 3


def fuzzy_segmentation_yellow_trapezoid(h):
    if 0 <= h <= 40 or 80 < h <= 360:
        return 0
    elif 40 < h <= 55:
        return (1 / 15) * h - 8 / 3
    elif 55 < h <= 65:
        return 1
    elif 65 < h <= 80:
        return (-1 / 15) * h + 11 / 3


def fuzzy_segmentation_green_trapezoid(h):
    if 0 <= h <= 65 or 170 < h <= 360:
        return 0
    elif 65 < h <= 80:
        return (1 / 15) * h - 8 / 3
    elif 80 < h <= 140:
        return 1
    elif 140 < h <= 170:
        return (-1 / 30) * h + 17 / 3


def fuzzy_segmentation_cyan_trapezoid(h):
    if 0 <= h <= 140 or 210 < h <= 360:
        return 0
    elif 140 < h <= 170:
        return (1 / 30) * h - 14 / 3
    elif 170 < h <= 200:
        return 1
    elif 200 < h <= 210:
        return -0.1 * h + 21


def fuzzy_segmentation_blue_trapezoid(h):
    if 0 <= h <= 200 or 270 < h <= 360:
        return 0
    elif 200 < h <= 210:
        return 0.1 * h - 20
    elif 210 < h <= 250:
        return 1
    elif 250 < h <= 270:
        return (-1 / 20) * h + 27 / 2


def fuzzy_segmentation_purple_trapezoid(h):
    if 0 <= h <= 250 or 330 < h <= 360:
        return 0
    elif 250 < h <= 270:
        return (1 / 20) * h - 5 / 4
    elif 270 < h <= 300:
        return 1
    elif 300 < h <= 330:
        return (-1 / 30) * h + 11
