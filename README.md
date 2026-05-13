# colorpack

This is a small utility package in Python to help with colors while plotting especially with **matplotlib**.

## Features

- Top level functions to create gradients and different shades of a color
- Easy integration into matplotlib

## Installation

Clone the GitHub repo and pip install:

```bash
git clone https://github.com/gthway/colorpack.git
cd colorpack
pip install -e .
```

## Quickstart


```python
from colorpack import shades, gradient, diverging, COLORS, PALETTES, PALETTE_NAMES
```

Named colors and color palettes that are natively available can be viewed with

```python
print(list(COLORS.keys()))
print(list(PALETTE_NAMES))
print(list(PALETTES))
```

**Creating shades of a color and gradient**

```python
shades_of_red = shades('red',5)
redblue_grad = gradient('red','blue',6)
redblue_diverging_grad = diverging('red','blue',6)  
```

**ColorSet class**

The `ColorSet` object allows easy use with matplotlib. You can create a colorset from the pre-defined list of color palettes or from a list of colors you input.

```python
cs = ColorSet('muted')
print(cs,cs.name,cs.colors,len(cs))
# Or use with the list created from shades
cs = ColorSet('shades_of_red')
print(cs,cs.name,cs.colors,len(cs))
```

The colorset created can be set as the prop cycle for matplotlib axes.

```python
fig, ax = plt.subplots()
cs.apply_to_axes(ax)
```