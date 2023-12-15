from img_dots import get_pixel_dots


def full_color(color: str) -> list:
    """ Returns a list of tuples with the pixel number and the color to fill
    the whole canvas with the same color."""
    print(f"Getting pixels to fill the canvas with {color}")
    return [(i, color) for i in range(0, 256)]


def image(img: str, color: str = None, bg_color: str = None) -> list:
    """ Returns a list of tuples with the pixel number and the color.

    Color is optional, if not provided, the color of the pixel will be the
    same as the image.

    When color is provided, all the pixels with opacity 255 will
    be replaced by the provided color.
    """
    return get_pixel_dots(img, color, bg_color)


def face_eyes_looking_to_left(eye_color: str) -> list:
    """ Pixel numbers and colors to draw eyes looking to the left. """
    print("Getting pixels to draw face with eyes looking to the left")
    return [(100, eye_color), (101, '#FFFFFF'),
            (105, eye_color), (106, '#FFFFFF')]


def face_eyes_looking_to_right(eye_color: str) -> list:
    """ Pixel numbers and colors to draw eyes looking to the right. """
    print(("Getting pixels to draw face with eyes looking to the right"))
    return [(100, '#FFFFFF'), (101, eye_color),
            (105, '#FFFFFF'), (106, eye_color)]


def face_close_eyes(face_color: str) -> list:
    """ Pixel numbers and colors to draw eyes closed. """
    print("Getting pixels to draw face with eyes closed")
    return [(100, face_color), (101, face_color),
            (105, face_color), (106, face_color)]
