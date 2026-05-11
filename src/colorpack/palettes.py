"""
palettes.py
-----------
Curated named color palettes stored as dictionaries of hex strings.
Each palette is a plain list so it can be sliced, iterated, or passed
directly to matplotlib.
"""

# ---------------------------------------------------------------------------
# Individual named colors (handy constants)
# ---------------------------------------------------------------------------

COLORS = {
    # Blues
    "cobalt":       "#0047AB",
    "sky":          "#87CEEB",
    "navy":         "#001F5B",
    "cornflower":   "#6495ED",
    "steel":        "#4682B4",
    "teal":         "#008080",
    "cyan":         "#00BCD4",
    # Greens
    "emerald":      "#50C878",
    "olive":        "#6B8E23",
    "sage":         "#8FAF8F",
    "mint":         "#AAF0D1",
    "forest":       "#228B22",
    "lime":         "#B5E550",
    # Reds / pinks
    "crimson":      "#DC143C",
    "rose":         "#FF6B8A",
    "blush":        "#FFB7C5",
    "scarlet":      "#FF2400",
    "burgundy":     "#800020",
    "coral":        "#FF6B6B",
    # Oranges / yellows
    "amber":        "#FFBF00",
    "tangerine":    "#F28500",
    "gold":         "#FFD700",
    "sand":         "#C2B280",
    "peach":        "#FFCBA4",
    # Purples
    "violet":       "#8A2BE2",
    "lavender":     "#B57EDC",
    "plum":         "#DDA0DD",
    "indigo":       "#4B0082",
    "mauve":        "#E0B0FF",
    # Neutrals
    "slate":        "#708090",
    "charcoal":     "#36454F",
    "smoke":        "#F5F5F5",
    "ivory":        "#FFFFF0",
    "espresso":     "#4B2C20",
}


# ---------------------------------------------------------------------------
# Curated palettes
# ---------------------------------------------------------------------------

PALETTES = {
    # A clean, professional set that works well for 5-10 lines
    "vivid": [
        "#E63946",  # red
        "#2196F3",  # blue
        "#4CAF50",  # green
        "#FF9800",  # orange
        "#9C27B0",  # purple
        "#00BCD4",  # cyan
        "#F06292",  # pink
        "#795548",  # brown
        "#607D8B",  # blue-grey
        "#CDDC39",  # lime
    ],

    # Muted / desaturated – great for academic papers
    "muted": [
        "#5D8AA8",  # air force blue
        "#E88B6F",  # terra cotta
        "#7CB883",  # fern
        "#C0A060",  # dark tan
        "#9B7AB8",  # amethyst
        "#5AACB8",  # cadet blue
        "#D47A8A",  # dark pink
        "#8C8C6E",  # grey-olive
        "#5888A0",  # slate blue
        "#B8A05A",  # dark khaki
    ],

    # High-contrast for presentations / posters
    "bold": [
        "#FF0000",  # pure red
        "#0000FF",  # pure blue
        "#00AA00",  # green
        "#FF8C00",  # dark orange
        "#8B008B",  # dark magenta
        "#008B8B",  # dark cyan
        "#FF1493",  # deep pink
        "#556B2F",  # dark olive
        "#4169E1",  # royal blue
        "#B8860B",  # dark goldenrod
    ],

    # Soft pastels – nice for filled areas / confidence bands
    "pastel": [
        "#FFB3BA",  # light pink
        "#FFDFBA",  # light peach
        "#FFFFBA",  # light yellow
        "#BAFFC9",  # light mint
        "#BAE1FF",  # light blue
        "#E8BAFF",  # light lavender
        "#FFD6BA",  # light orange
        "#C9FFBA",  # light green
        "#FFBAE1",  # light rose
        "#BAF0FF",  # light cyan
    ],

    # Colorblind-friendly (based on Wong 2011 palette)
    "colorblind": [
        "#E69F00",  # orange
        "#56B4E9",  # sky blue
        "#009E73",  # green
        "#F0E442",  # yellow
        "#0072B2",  # blue
        "#D55E00",  # vermillion
        "#CC79A7",  # pink
        "#000000",  # black
    ],

    # Earthy / natural tones
    "earth": [
        "#8B5E3C",  # brown
        "#6B8E23",  # olive
        "#C2956C",  # sand
        "#4A7C59",  # moss
        "#9E6B4A",  # clay
        "#D4A853",  # ochre
        "#557A55",  # fern
        "#A0785A",  # raw umber
        "#7A9E7E",  # sage
        "#C4955A",  # caramel
    ],

    # Cool blues and teals for scientific / ocean data
    "ocean": [
        "#003F5C",
        "#2C7BB6",
        "#00A6CA",
        "#00CCBC",
        "#90EB9D",
        "#26C6DA",
        "#0288D1",
        "#0077B6",
        "#48CAE4",
        "#ADE8F4",
    ],

    # Warm sunset tones
    "sunset": [
        "#FF6B6B",
        "#FE8C5A",
        "#FFA94D",
        "#FFD166",
        "#F7B731",
        "#E55039",
        "#D35400",
        "#C0392B",
        "#E91E63",
        "#FF5722",
    ],
}

# Convenience: all palette names
PALETTE_NAMES = list(PALETTES.keys())
