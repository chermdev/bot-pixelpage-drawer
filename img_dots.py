from PIL import Image


def rgb_to_hex(rgba: str):
    """ Returns the hex value of an rgba color. """
    r, g, b, _ = rgba
    hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex.upper()


def get_pixel_dots(img: str, color: str = None, bg_color: str = None):
    """ Returns a list of tuples with the pixel number and the color. """
    print(f"Getting pixels from {img}")
    img = Image.open(img)
    dots = list(img.getdata())
    colors = []
    for i in range(len(dots)):
        if dots[i][3] == 255:
            if not color:
                colors.append((i, rgb_to_hex(dots[i])))
            else:
                colors.append((i, color))
        elif bg_color:
            colors.append((i, bg_color))
    print(f"Got {len(colors)} pixels from {img}")
    return colors
