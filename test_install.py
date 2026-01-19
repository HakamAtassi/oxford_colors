#!/usr/bin/env python3
"""
Test script to verify the oxford_colors package works correctly.
"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

try:
    from oxford_colors import oxford_style, OXFORD_COLORS, hex, rgb
    print("✓ Successfully imported oxford_colors")
except ImportError as e:
    print(f"✗ Failed to import oxford_colors: {e}")
    sys.exit(1)

# Test basic functionality
try:
    # Test color access
    blue_hex = hex("oxford_blue")
    blue_rgb = rgb("oxford_blue")
    print(f"✓ Oxford blue: {blue_hex} {blue_rgb}")
    
    # Test context manager
    with oxford_style():
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        ax.plot([1, 2, 3], [1, 2, 3])
        plt.savefig('test_output.png', dpi=100, bbox_inches='tight')
        plt.close()
    print("✓ Context manager works correctly")
    
    # Test custom colors
    with oxford_style(colors=["oxford_blue", "oxford_pink"]):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        plt.savefig('test_custom.png', dpi=100, bbox_inches='tight')
        plt.close()
    print("✓ Custom colors work correctly")
    
    print("\n🎉 All tests passed! oxford_colors is working correctly.")
    
except Exception as e:
    print(f"✗ Test failed: {e}")
    sys.exit(1)
