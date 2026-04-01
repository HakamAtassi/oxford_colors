"""
graph_container.py
Bundles a graph's source file, variables, and figure into a zip archive.
"""

from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime
from typing import Optional, Union
import inspect
import pathlib
import warnings
import zipfile
import matplotlib.pyplot as plt


__all__ = ["containerize"]


@contextmanager
def containerize(
    output_path: Optional[Union[str, pathlib.Path]] = None,
    files: Optional[list] = None,
):
    """
    Context manager that zips up:
      - the current .py / .ipynb source file
      - all user variables at the time the block exits
      - any figure(s) saved via plt.savefig() inside the block
      - any extra files passed via ``files``

    Parameters
    ----------
    output_path : str or Path, optional
        Destination for the zip (extension ignored). Defaults to a
        timestamp-based name in the current directory.
    files : list, optional
        Extra files to include in the zip.

    Example
    -------
    with containerize("my_plot"):
        plt.plot(x, y)
        plt.savefig("my_plot.png", dpi=300)
    """
    if output_path is None:
        base_path = pathlib.Path(datetime.now().strftime("graph_%Y%m%d_%H%M%S"))
        warnings.warn(
            "containerize() called without output_path; output will be saved as "
            f"'{base_path}.zip' in the current directory.",
            UserWarning,
            stacklevel=2,
        )
    else:
        base_path = pathlib.Path(output_path)

    base_path.parent.mkdir(parents=True, exist_ok=True)

    _saved_figures: list[pathlib.Path] = []
    _orig_savefig = plt.savefig

    def _track(fname, *args, **kwargs):
        _orig_savefig(fname, *args, **kwargs)
        if isinstance(fname, (str, pathlib.Path)):
            _saved_figures.append(pathlib.Path(fname))

    plt.savefig = _track
    try:
        yield
    finally:
        plt.savefig = _orig_savefig
        _build_zip(base_path, _saved_figures, files or [])


# ---------------------------------------------------------------------------

def _user_frame():
    """Walk the call stack to find the first frame outside this module."""
    frame = inspect.currentframe()
    while frame is not None:
        fname = frame.f_code.co_filename
        if (
            not fname.endswith("graph_container.py")
            and "site-packages" not in fname
            and "contextlib" not in fname
        ):
            return frame
        frame = frame.f_back
    return None


def _source_file(frame) -> Optional[pathlib.Path]:
    """Return the .py or .ipynb file being executed, or None."""
    # VS Code Jupyter stores the notebook path here
    vsc = (frame.f_globals or {}).get("__vsc_ipynb_file__")
    if vsc:
        p = pathlib.Path(vsc)
        if p.exists():
            return p

    p = pathlib.Path(frame.f_code.co_filename)
    if p.suffix == ".py" and p.exists():
        return p

    return None


def _write_vars(frame, path: pathlib.Path):
    """Write all user-defined variables to a Python file using repr()."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Variables captured: {datetime.now().isoformat()}\n\n")
        for name, value in frame.f_locals.items():
            if name.startswith("_"):
                continue
            if inspect.ismodule(value) or inspect.isfunction(value) or inspect.isclass(value):
                continue
            try:
                f.write(f"{name} = {repr(value)}\n")
            except Exception:
                continue


def _build_zip(base_path: pathlib.Path, figures: list, extra_files: list):
    frame = _user_frame()
    stem = base_path.stem
    parent = base_path.parent

    vars_path = parent / f"{stem}_vars.py"
    if frame:
        _write_vars(frame, vars_path)

    source = _source_file(frame) if frame else None

    zip_path = parent / f"{stem}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        if source and source.exists():
            zf.write(source, source.name)
            print(f"  + {source.name}")
        if vars_path.exists():
            zf.write(vars_path, vars_path.name)
            print(f"  + {vars_path.name}")
        for fig in figures:
            if fig.exists():
                zf.write(fig, fig.name)
                print(f"  + {fig.name}")
            else:
                print(f"  ! missing figure, skipping: {fig}")
        for extra in extra_files:
            p = pathlib.Path(extra)
            if p.exists():
                zf.write(p, p.name)
                print(f"  + {p.name}")
            else:
                print(f"  ! missing file, skipping: {p}")

    print(f"Container: {zip_path}")

    try:
        vars_path.unlink()
    except Exception:
        pass
