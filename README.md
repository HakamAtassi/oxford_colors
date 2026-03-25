# Oxford Colors

A Python library providing Oxford University's official color palette for matplotlib visualizations.

## Installation

```bash
pip install oxford_colors
```

## Quick Start

```python
import matplotlib.pyplot as plt
from oxford_colors import oxford_style

# Apply Oxford colors with the context manager
with oxford_style():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    ax.plot([1, 2, 3], [1, 2, 3])
    plt.show()
```

## Features

- **Official Oxford Colors**: Complete palette including primary, secondary, neutral, and metallic colors
- **Context Manager**: Temporary color styling that automatically restores previous rcParams
- **Custom Color Selection**: Choose specific colors from the palette
- **Multiple Plot Types**: Works with line plots, bar charts, scatter plots, histograms, and more
- **Matplotlib Integration**: Seamless integration with matplotlib's color cycle
- **Color Metadata**: Access hex, RGB, CMYK, and Pantone values for every color

## Available Colors

### Primary
| Key | Name | Hex |
|-----|------|-----|
| `oxford_blue` | Oxford blue | `#002147` |

### Secondary
| Key | Name | Hex |
|-----|------|-----|
| `oxford_mauve` | Oxford mauve | `#776885` |
| `oxford_peach` | Oxford peach | `#E08D79` |
| `oxford_potters_pink` | Oxford potters pink | `#ED9390` |
| `oxford_dusk` | Oxford dusk | `#C4A29E` |
| `oxford_lilac` | Oxford lilac | `#D1BDD5` |
| `oxford_sienna` | Oxford sienna | `#994636` |
| `oxford_ccb_red` | Oxford Red | `#AA1A2D` |
| `oxford_plum` | Oxford plum | `#7F055F` |
| `oxford_coral` | Oxford coral | `#FE615A` |
| `oxford_lavender` | Oxford lavender | `#D4CDF4` |
| `oxford_orange` | Oxford orange | `#FB5607` |
| `oxford_pink` | Oxford pink | `#E6007E` |
| `oxford_green` | Oxford green | `#426A5A` |
| `oxford_ocean_grey` | Oxford ocean grey | `#789E9E` |
| `oxford_yellow_ochre` | Oxford yellow ochre | `#E2C044` |
| `oxford_cool_grey` | Oxford cool grey | `#E4F0EF` |
| `oxford_sky_blue` | Oxford sky blue | `#B9D6F2` |
| `oxford_sage_green` | Oxford sage green | `#A0AF84` |
| `oxford_viridian` | Oxford viridian | `#15616D` |
| `oxford_royal_blue` | Oxford royal blue | `#1D42A6` |
| `oxford_aqua` | Oxford aqua | `#00AAB4` |
| `oxford_vivid_green` | Oxford vivid green | `#65E5AE` |
| `oxford_lime_green` | Oxford lime green | `#95C11F` |
| `oxford_cerulean_blue` | Oxford cerulean blue | `#49B6FF` |
| `oxford_yellow` | Oxford lemon yellow | `#F7EF66` |

### Neutrals
| Key | Name | Hex |
|-----|------|-----|
| `oxford_charcoal` | Oxford charcoal | `#211D1C` |
| `oxford_ash_grey` | Oxford ash grey | `#61615F` |
| `oxford_umber` | Oxford umber | `#89827A` |
| `oxford_stone_grey` | Oxford stone grey | `#D9D8D6` |
| `oxford_shell_grey` | Oxford shell grey | `#F1EEE9` |
| `oxford_off_white` | Oxford off white | `#F2F0F0` |

### Metallic
| Key | Name | Hex |
|-----|------|-----|
| `oxford_gold` | Oxford gold | `#C9A14B` |
| `oxford_silver` | Oxford silver | `#BFC0C0` |

## API Reference

### Context Manager

#### `oxford_style(colors=None)`

Apply Oxford colors temporarily. Restores previous matplotlib rcParams on exit.

```python
from oxford_colors import oxford_style

# Default Oxford palette
with oxford_style():
    plt.plot(...)

# Specific colors only
with oxford_style(colors=["oxford_blue", "oxford_pink", "oxford_green"]):
    plt.plot(...)
```

Also supports subscript access to look up hex values:

```python
oxford_style["oxford_blue"]   # -> '#002147'
oxford_style["oxford_pink"]   # -> '#E6007E'
```

### Color Accessors

```python
from oxford_colors import hex, rgb, cmyk, pantone, as_rgb_norm

hex("oxford_blue")        # -> '#002147'
rgb("oxford_blue")        # -> (0, 33, 71)
cmyk("oxford_blue")       # -> (100, 87, 42, 51)
pantone("oxford_blue")    # -> 'Pantone 282'
as_rgb_norm("oxford_blue")  # -> (0.0, 0.129, 0.278)  (normalized 0..1 for matplotlib)
```

### Color Discovery

```python
from oxford_colors import get_names, OXFORD_COLORS, COLORS_BY_GROUP

# All color keys (sorted)
get_names()

# Colors in a specific group: 'primary', 'secondary', 'neutrals', 'metallic'
get_names("secondary")

# Full Color objects (with .name, .hex, .rgb, .cmyk, .pantone attributes)
OXFORD_COLORS["oxford_blue"].name     # -> 'Oxford blue'
OXFORD_COLORS["oxford_blue"].pantone  # -> 'Pantone 282'

# Colors grouped by category
COLORS_BY_GROUP["primary"]   # -> ['oxford_blue']
COLORS_BY_GROUP["metallic"]  # -> ['oxford_gold', 'oxford_silver']
```

### Matplotlib Helpers

```python
from oxford_colors import mpl_palette, mpl_cycler, set_plt_colors, DEFAULT_PALETTE
import matplotlib.pyplot as plt

# List of hex strings for a set of colors
mpl_palette(["oxford_blue", "oxford_pink", "oxford_green"])

# Default palette (all colors ordered by "Oxford-ness")
DEFAULT_PALETTE

# matplotlib cycler object
plt.rcParams['axes.prop_cycle'] = mpl_cycler(["oxford_blue", "oxford_pink"])

# Convenience: set colors on an existing plt instance
set_plt_colors(plt, ["oxford_blue", "oxford_pink", "oxford_green"])
```

## Usage Examples

### Basic Line Plot

```python
import matplotlib.pyplot as plt
from oxford_colors import oxford_style

with oxford_style():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 8], label='Series 1')
    ax.plot([1, 2, 3, 4], [2, 3, 4, 5], label='Series 2')
    ax.legend()
    plt.show()
```

### Bar Chart

```python
import matplotlib.pyplot as plt
from oxford_colors import oxford_style

with oxford_style():
    fig, ax = plt.subplots()
    ax.bar(['A', 'B', 'C', 'D'], [23, 45, 56, 78])
    plt.show()
```

### Scatter Plot

```python
import numpy as np
import matplotlib.pyplot as plt
from oxford_colors import oxford_style

with oxford_style():
    fig, ax = plt.subplots()
    ax.scatter(np.random.randn(50), np.random.randn(50), alpha=0.7)
    plt.show()
```

### Multiple Subplots

```python
import matplotlib.pyplot as plt
import numpy as np
from oxford_colors import oxford_style

with oxford_style():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

    x = np.linspace(0, 10, 100)
    ax1.plot(x, np.sin(x))
    ax1.set_title('Sine Wave')

    ax2.scatter(np.random.randn(50), np.random.randn(50))
    ax2.set_title('Scatter Plot')

    ax3.bar(['A', 'B', 'C'], [10, 20, 15])
    ax3.set_title('Bar Chart')

    ax4.hist(np.random.normal(0, 1, 1000), bins=30)
    ax4.set_title('Histogram')

    plt.tight_layout()
    plt.show()
```

### Setting Colors Globally

```python
import matplotlib.pyplot as plt
from oxford_colors import set_plt_colors

set_plt_colors(plt)  # applies default Oxford palette globally

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

## Development

### Setup

```bash
git clone https://github.com/HakamAtassi/oxford_colors.git
cd oxford_colors
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Building the Package

```bash
python -m build
```

## Gallery

The `examples/gallery.py` script generates a comprehensive gallery of plots using Oxford colors:

```bash
python -m oxford_colors.examples.gallery
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Color References

The colors in this library are based on Oxford University's official brand guidelines and include:
- Official Pantone references where available
- CMYK values for print applications
- RGB values for digital use
- Hex codes for web applications

## Changelog

### Version 1.1.0
- Extended secondary palette (added `oxford_cool_grey`, `oxford_sky_blue`, `oxford_sage_green`, `oxford_viridian`, `oxford_royal_blue`, `oxford_aqua`, `oxford_vivid_green`, `oxford_lime_green`, `oxford_cerulean_blue`, `oxford_yellow`)
- Added `cmyk`, `pantone`, `as_rgb_norm`, `get_names`, `mpl_cycler`, `set_plt_colors` helpers
- Added `COLORS_BY_GROUP` for group-based color discovery
- `oxford_style` now supports subscript color lookup

### Version 1.0.0
- Initial release
- Core Oxford color palette
- Context manager for temporary styling
- Comprehensive test suite
- PyPI distribution ready
