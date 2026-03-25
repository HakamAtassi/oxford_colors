"""
Gallery of example plots using Oxford Colors.
Run this script to regenerate all example images in the examples/ folder.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from oxford_colors import oxford_style, DEFAULT_PALETTE

OUT = Path(__file__).parent

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
scatter_x = np.random.randn(50)
scatter_y = np.random.randn(50)
hist_data = np.random.normal(0, 1, 1000)


def create_line_plot():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y1, label='sin(x)', linewidth=2)
        ax.plot(x, y2, label='cos(x)', linewidth=2)
        ax.plot(x, y3, label='sin(x)cos(x)', linewidth=2)
        ax.plot(x, y1 + y2, label='sin(x)+cos(x)', linewidth=2)
        ax.plot(x, y1 - y2, label='sin(x)-cos(x)', linewidth=2)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Line Plot with Oxford Colors')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT / 'line_plot.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_line_plot_with_markers():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x[::5], y1[::5], 'o-', label='sin(x)', markersize=6, linewidth=2)
        ax.plot(x[::5], y2[::5], 's-', label='cos(x)', markersize=6, linewidth=2)
        ax.plot(x[::5], y3[::5], '^-', label='sin(x)cos(x)', markersize=6, linewidth=2)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Line Plot with Markers')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT / 'line_plot_markers.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_scatter_plot():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(scatter_x, scatter_y, alpha=0.7, s=60)
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')
        ax.set_title('Scatter Plot')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT / 'scatter_plot.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_scatter_plot_colored():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        colors = np.random.rand(len(scatter_x))
        scatter = ax.scatter(scatter_x, scatter_y, c=colors, alpha=0.7, s=60, cmap='viridis')
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')
        ax.set_title('Colored Scatter Plot')
        ax.grid(True, alpha=0.3)
        plt.colorbar(scatter, label='Color Scale')
        plt.tight_layout()
        plt.savefig(OUT / 'scatter_plot_colored.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_bar_chart():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(categories, values)
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_title('Bar Chart')
        ax.grid(True, alpha=0.3, axis='y')
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 1,
                    f'{value}', ha='center', va='bottom')
        plt.tight_layout()
        plt.savefig(OUT / 'bar_chart.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_horizontal_bar_chart():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(categories, values)
        ax.set_xlabel('Values')
        ax.set_ylabel('Categories')
        ax.set_title('Horizontal Bar Chart')
        ax.grid(True, alpha=0.3, axis='x')
        for bar, value in zip(bars, values):
            ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2.,
                    f'{value}', ha='left', va='center')
        plt.tight_layout()
        plt.savefig(OUT / 'horizontal_bar_chart.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_histogram():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        ax.hist(hist_data, bins=30, alpha=0.7, edgecolor='black')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram')
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(OUT / 'histogram.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_multiple_histograms():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        ax.hist(np.random.normal(0, 1, 1000), bins=30, alpha=0.7, label='Dataset 1')
        ax.hist(np.random.normal(2, 1.5, 1000), bins=30, alpha=0.7, label='Dataset 2')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_title('Multiple Histograms')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(OUT / 'multiple_histograms.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_subplots():
    with oxford_style():
        _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        ax1.plot(x, y1, linewidth=2)
        ax1.set_title('Line Plot')
        ax1.grid(True, alpha=0.3)
        ax2.scatter(scatter_x, scatter_y, alpha=0.7, s=60)
        ax2.set_title('Scatter Plot')
        ax2.grid(True, alpha=0.3)
        ax3.bar(categories, values)
        ax3.set_title('Bar Chart')
        ax3.grid(True, alpha=0.3, axis='y')
        ax4.hist(hist_data, bins=20, alpha=0.7)
        ax4.set_title('Histogram')
        ax4.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(OUT / 'subplots.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_custom_colors():
    with oxford_style(["oxford_blue", "oxford_pink", "oxford_green", "oxford_orange"]):
        _, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y1, label='sin(x)', linewidth=2)
        ax.plot(x, y2, label='cos(x)', linewidth=2)
        ax.plot(x, y3, label='sin(x)cos(x)', linewidth=2)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Custom Oxford Colors')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT / 'custom_colors.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_many_lines():
    with oxford_style():
        _, ax = plt.subplots(figsize=(12, 8))
        for i in range(25):
            ax.plot(x, np.sin(x + i * 0.3) * (1 + i * 0.05), alpha=0.8, linewidth=1.5)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('25 Lines with Unique Oxford Colors')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT / 'many_lines.png', dpi=300, bbox_inches='tight')
        plt.close()


def create_stacked_bar():
    with oxford_style():
        _, ax = plt.subplots(figsize=(10, 6))
        quarters = ['Q1', 'Q2', 'Q3', 'Q4']
        v1 = [20, 35, 30, 35]
        v2 = [25, 25, 15, 20]
        v3 = [15, 20, 25, 15]
        ax.bar(quarters, v1, 0.6, label='Product A')
        ax.bar(quarters, v2, 0.6, bottom=v1, label='Product B')
        ax.bar(quarters, v3, 0.6, bottom=np.array(v1) + np.array(v2), label='Product C')
        ax.set_xlabel('Quarter')
        ax.set_ylabel('Sales')
        ax.set_title('Stacked Bar Chart')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(OUT / 'stacked_bar.png', dpi=300, bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    plots = [
        (create_line_plot,              "line_plot"),
        (create_line_plot_with_markers, "line_plot_markers"),
        (create_scatter_plot,           "scatter_plot"),
        (create_scatter_plot_colored,   "scatter_plot_colored"),
        (create_bar_chart,              "bar_chart"),
        (create_horizontal_bar_chart,   "horizontal_bar_chart"),
        (create_histogram,              "histogram"),
        (create_multiple_histograms,    "multiple_histograms"),
        (create_subplots,               "subplots"),
        (create_custom_colors,          "custom_colors"),
        (create_many_lines,             "many_lines"),
        (create_stacked_bar,            "stacked_bar"),
    ]

    print(f"Saving to {OUT}/")
    for fn, name in plots:
        fn()
        print(f"  {name}.png")
    print(f"\nDone — {len(plots)} plots, {len(DEFAULT_PALETTE)} colors available.")
