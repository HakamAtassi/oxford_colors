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
import pickle
import warnings
import zipfile
import matplotlib.pyplot as plt


__all__ = ["containerize"]


@contextmanager
def containerize(
    output_path: Optional[Union[str, pathlib.Path]] = None,
    files: Optional[list] = None,
    variables: Optional[list] = None,
):
    """
    Context manager that zips up:
      - the calling .py source file
      - any figures saved via plt.savefig() inside the block
      - any extra files passed via ``files``
      - any explicitly passed ``variables``

    Parameters
    ----------
    output_path : str or Path, optional
        Destination for the zip (extension ignored). Defaults to a
        timestamp-based name in the current directory.
    files : list, optional
        Extra files to include in the zip.
    variables : list, optional
        Variables to store, e.g. ``[x, y]``.

    Example
    -------
    with containerize("my_plot", variables=[x, y]):
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
        _build_zip(base_path, _saved_figures, files or [], variables or {})


# ---------------------------------------------------------------------------

def _caller_source() -> Optional[pathlib.Path]:
    """Walk the call stack to find the .py or .ipynb source file."""
    for frame_info in inspect.stack():
        frame = frame_info.frame
        fname = frame_info.filename

        if (
            fname.endswith("graph_container.py")
            or "site-packages" in fname
            or "contextlib" in fname
        ):
            continue

        # VS Code Jupyter stores the notebook path here
        vsc = (frame.f_globals or {}).get("__vsc_ipynb_file__")
        if vsc:
            p = pathlib.Path(vsc)
            if p.exists():
                return p

        p = pathlib.Path(fname)
        if p.suffix == ".py" and p.exists():
            return p

    return None


def _pickle_vars(variables: list, path: pathlib.Path):
    """Pickle explicitly passed variables to a .pkl file."""
    with open(path, "wb") as f:
        pickle.dump(variables, f, protocol=pickle.HIGHEST_PROTOCOL)


def _build_zip(base_path: pathlib.Path, figures: list, extra_files: list, variables: list):
    stem = base_path.stem
    parent = base_path.parent

    source = _caller_source()

    vars_path = None
    if variables:
        vars_path = parent / f"{stem}_vars.pkl"
        _pickle_vars(variables, vars_path)

    zip_path = parent / f"{stem}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        if source and source.exists():
            zf.write(source, source.name)
            print(f"  + {source.name}")
        if vars_path and vars_path.exists():
            zf.write(vars_path, vars_path.name)
            print(f"  + {vars_path.name}  (pickle)")
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

    if vars_path:
        try:
            vars_path.unlink()
        except Exception:
            pass
