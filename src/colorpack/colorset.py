from typing import List, Optional
import itertools
import random

from .palettes import COLORS, PALETTES, PALETTE_NAMES
from .gradients import shades, gradient, diverging

class ColorSet:
    """
    A color picker object.
    """

    def __init__(self,palette):
        if isinstance(palette,str):
            palette = palette.lower()
            if palette not in PALETTE_NAMES:
                raise ValueError(f'Unknown palette. Use a named palette or enter a custom list of hex strings.')
            self.name = palette
            self.colors = list(PALETTES[palette])

        elif isinstance(palette,list):
            for c in palette:
                if not isinstance(c, str) or not c.startswith("#"):
                    raise ValueError(f"Expected hex color strings, got: {c!r}")
            self.name = "custom"
            self.colors = list(palette)

    # Helpers
    def __repr__(self) -> str:
        return f"ColorSet(palette='{self.name}',n={len(self.colors)})"

    def __len__(self) -> int:
        return len(self.colors)
    
    def __getitem__(self,idx):
        return self.colors[idx]

    def __iter__(self):
        return iter(self.colors)

    def pick(self,n) -> List[str]:
        """Return the first n colors from the palette. If n is larger than the number of colors in palette, the list is cycled automatically."""
        if n <= 0:
            raise ValueError(f'n must be a positive integer')
        return list(itertools.islice(itertools.cycle(self.colors),n))

    def cycle(self,n):
        """Same as self.pick."""
        return self.pick(n)

    def random(self,n,seed=None):
        """Sample n random colors from the palette."""
        rng = random.Random(seed)
        if n <= len(self.colors):
            return rng.sample(self.colors,n)
        # if n > palette size, pick with replacement
        else:
            return [rng.choice(self.colors) for _ in range(n)]

    def evenly_spaced(self,n):
        """Returns n evenly spaced colors from the palette."""
        m = len(self.colors)
        if n > m:
            raise ValueError(f'Palette only has {m} colors. Use .pick() instead')
        
        indices = [round(i * (m - 1) / (n - 1)) for i in range(n)]
        return [self.colors[i] for i in indices]

    def shades(self, color: str, n: int = 6, **kwargs) -> List[str]:
        """
        Generate *n* shades of *color*. Thin wrapper around
        :func:`mplcolors.shades`.
        """
        return shades(color, n, **kwargs)

    def gradient(self, start: str, end: str, n: int = 6) -> List[str]:
        """
        Linear RGB gradient from *start* to *end* with *n* steps.
        Thin wrapper around :func:`mplcolors.gradient`.
        """
        return gradient(start, end, n)

    # For use with Matplotlib

    def as_cycler(self, n: Optional[int] = None):
        """
        Return a ``cycler`` object that can be passed to
        ``matplotlib.pyplot.rc('axes', prop_cycle=cs.as_cycler())``.

        Requires the ``cycler`` package (installed with matplotlib).

        Parameters
        ----------
        n : int, optional
            Use only the first *n* colors. Defaults to the full palette.
        """
        try:
            from cycler import cycler as _cycler
        except ImportError:
            raise ImportError(
                "The 'cycler' package is required. "
                "Install it with: pip install cycler"
            )
        colors = self._colors if n is None else self.pick(n)
        return _cycler(color=colors)

    def apply_to_axes(self, ax, n: Optional[int] = None) -> None:
        """
        Set the color cycle of a matplotlib ``Axes`` object.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        n : int, optional
            Use first *n* palette colors.

        Examples
        --------
        >>> fig, ax = plt.subplots()
        >>> cs.apply_to_axes(ax)
        """
        ax.set_prop_cycle(self.as_cycler(n))


    # Print summary

    def info(self) -> None:
        """Print a brief summary of the palette."""
        print(f"ColorSet — palette: '{self._name}' ({len(self._colors)} colors)")
        for i, c in enumerate(self._colors):
            print(f"  [{i:2d}]  {c}")