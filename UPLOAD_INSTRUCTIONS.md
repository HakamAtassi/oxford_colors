# PyPI Upload Instructions

## Prerequisites

1. Install twine for uploading:
```bash
pip install twine
```

2. Have your PyPI credentials ready (or use an API token)

## Test Upload (Recommended)

First upload to TestPyPI to verify everything works:

```bash
twine upload --repository testpypi dist/*
```

Install from TestPyPI to verify:
```bash
pip install --index-url https://test.pypi.org/simple/ oxford_colors
```

## Production Upload

Once verified, upload to the real PyPI:

```bash
twine upload dist/*
```

## Verification

After upload, verify installation:
```bash
pip install oxford_colors
python -c "from oxford_colors import oxford_style; print('✓ Installation successful!')"
```

## Package Contents

The package includes:
- Core library with Oxford color palette
- Context manager for temporary styling
- Example gallery generator
- Comprehensive test suite
- Full documentation

## Version Management

- Current version: 1.0.0
- Update version in `pyproject.toml` before new releases
- Tag releases in Git for better tracking

## Notes

- The package supports Python 3.8+
- Requires matplotlib and numpy as dependencies
- All tests pass successfully
- Example gallery generates 11 different plot types
