import colorsys
from typing import List, Tuple

from .palettes import COLORS

def _sense_colorhex(color:str) -> str:
    """    
    Returns the hex string of a named color in colorpack.COLORS.
    """    
    lookup = color.lower()
    if lookup in COLORS:
        hexcode = COLORS[lookup]
    else:
        raise ValueError(
            f"Unknown color name '{color}'."
            f"Use a hexstring or a color available in COLORS."
        )
    return hexcode

def _parse_color(color: str) -> Tuple[float,float,float]:
    """
    Accepts either a named color in colorpack.COLORS or a hex string and coverts it into a RGB tuple with values between [0,1].
    """

    if not color.startswith('#'):
        color = _sense_colorhex(color)

    color = color.lstrip('#')
    if len(color) != 6:
        raise ValueError(f"Invalid hex color '{color}'. Expected format: #RRGGBB")

    r = int(color[0:2],16)/255
    g = int(color[2:4],16)/255
    b = int(color[4:6],16)/255

    return r,g,b

def _rgb_to_hex(r:float,g:float,b:float) -> str:
    """
    Converts RGB tuple with values between [0,1] to a hex string.
    """
    
    red = round(r*255)
    green = round(g*255)
    blue = round(b*255)
    hexstr = "#{:02X}{:02X}{:02X}".format(red,green,blue)
    return hexstr


def gradient(start:str, end:str, n:int = 6) -> List[str]:
    """
    Returns a linearly interpolated gradient of n colors.
    """
    if n < 2:
        raise ValueError(f"n cannot must be at least 2 colors")
    r1,g1,b1 = _parse_color(start)
    r2,g2,b2 = _parse_color(end)

    result = []
    for i in range(n):
        t = i / (n-1)
        r = r1 + t*(r2-r1)
        g = g1 + t*(g2-g1)
        b = b1 + t*(b2-b1)
        result.append(_rgb_to_hex(r,g,b))
    
    return result

def shades(color:str, n:int =6,*, lightest:float = 0.85,darkest:float =0.25) -> List[str]:
    """
    Returns n different shades of the input color.
    """
    if n < 2:
        raise ValueError("n must be at least 2.")
    if not (0 < darkest < lightest < 1):
        raise ValueError("Must satisfy 0 < darkest < lightest < 1.")
    
    r,g,b = _parse_color(color)
    h, _, s = colorsys.rgb_to_hls(r,g,b)

    step = (lightest - darkest)/ (n-1)

    result = []
    for i in range(n):
        l = lightest - i*step
        r,g,b = colorsys.hls_to_rgb(h,l,s)
        result.append(_rgb_to_hex(r,g,b))
    return result

def diverging(low:str,high:str,n:int=7,mid:str='#FFFFFF'):
    """    
    Gives a diverging gradient from two input colors.    
    """    
    half = n+1//2
    left = gradient(low,mid,half)
    right = gradient(mid,high,half)
    return left + right[1:]