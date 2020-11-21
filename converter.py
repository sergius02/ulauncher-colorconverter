def get_int_tuple(values: str):
    return tuple(map(int, values.replace('(', '').replace(')', '').replace(' ', '').split(',')))


def get_float_tuple(values: str):
    return tuple(map(float, values.replace('(', '').replace(')', '').replace(' ', '').split(',')))


def normalize_hexadecimal(hex: str):
    if not hex.__contains__('#'):
        return '#' + hex
    else:
        return hex


# Thanks to https://www.w3resource.com/python-exercises/math/python-math-exercise-77.php
def rgb_to_hsv(rgb: tuple):
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return round(h, 1), round(s, 1), round(v, 1)


# Thanks to https://www.rapidtables.com/convert/color/hsv-to-rgb.html
def hsv_to_rgb(hsv: tuple):
    h, s, v = hsv[0], hsv[1]/100, hsv[2]/100
    c: float = v * s
    x: float = c * (1 - abs((h/60) % 2 - 1))
    m: float = v - c

    r, g, b = 0, 0, 0
    if 0 <= h < 60:
        r = c
        g = x
        b = 0
    elif 60 <= h < 120:
        r = x
        g = c
        b = 0
    elif 120 <= h < 180:
        r = 0
        g = c
        b = x
    elif 180 <= h < 240:
        r = 0
        g = x
        b = c
    elif 240 <= h < 300:
        r = x
        g = 0
        b = c
    elif 300 <= h < 360:
        r = c
        g = 0
        b = x

    return int((r+m)*255), int((g+m)*255), int((b+m)*255)

# Thanks to https://ariya.blogspot.com/2008/07/converting-between-hsl-and-hsv.html
def hsv_to_hsl(hsv: tuple):
    h, s, v = hsv[0], hsv[1]/100, hsv[2]/100

    hh = h
    ll = (2.0 - s) * v
    ss = s * v
    if ll <= 1:
        ss /= ll
    else:
        ss /= 2 - ll
    ll /= 2

    return round(hh, 0), round(ss * 100, 1), round(ll * 100, 1)

# Thanks to https://ariya.blogspot.com/2008/07/converting-between-hsl-and-hsv.html
def hsl_to_hsv(hsl: tuple):
    hh, ss, ll = hsl[0], hsl[1]/100, hsl[2]/100
    h, s, l = 0, 0, 0

    h = hh
    ll *= 2
    if ll <= 1:
        ss *= ll
    else:
        ss *= 2 - ll
    v = (ll + ss) / 2
    s = (2 * ss) / (ll + ss)

    return round(h, 0), round(s * 100, 1), round(v * 100, 1)


def rgb_to_hex(rgb: tuple):
    return '#%02x%02x%02x' % rgb


def hex_to_rgb(hex: str):
    hex = hex.replace("#", "")
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_cmyk(rgb: tuple):
    r, g, b = rgb[0]/255, rgb[1]/255, rgb[2]/255

    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)

    return round(c * 100, 1), round(m * 100, 1), round(y * 100, 1), round(k * 100, 1)

def cmyk_to_rgb(cmyk: tuple):
    c, m, y, k = cmyk[0]/100, cmyk[1]/100, cmyk[2]/100, cmyk[3]/100

    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    return int(r), int(g), int(b)
