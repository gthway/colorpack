from colorpack.gradients import _parse_color, _rgb_to_hex, gradient, shades, diverging
from colorpack.palettes import COLORS, PALETTES
from colorpack.colorset import ColorSet

print(shades('red',5))
print(gradient('red','blue',7))
print(diverging('red','blue',5))