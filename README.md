# colorpack

This is a small utility package in Python to help with colors while plotting especially with **matplotlib**.

## Features

## Installation

## Quickstart


```python
from colorpack import shades, gradient, diverging, COLORS, PALETTES
```

Named colors and color palettes that are natively available can be viewed with

```python
print(list(COLORS.keys()))
print(list(PALETTES.keys()))
```

**Creating shades of a color and gradient**

```python
shades_of_red = shades('#FF0000',5) # Can also use with named colors 
  
```