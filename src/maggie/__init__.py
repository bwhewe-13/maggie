"""MAGGIE - Mesh-Agnostic Graphics for Group-wise Iteration and Evolution.

A PySide6 (Qt) tool for loading and visualizing neutron flux data.

Only the Qt-free surface (the flux model and array IO) is exported here, so
``import maggie`` never pulls in Qt. The GUI lives in ``maggie.gui`` and
is launched via ``maggie.app.main``.
"""

from maggie.core.flux_model import FluxModel
from maggie.io.arrays import ArrayInfo, list_arrays, load_array

__version__ = "0.1.0"

__all__ = ["FluxModel", "ArrayInfo", "list_arrays", "load_array", "__version__"]
