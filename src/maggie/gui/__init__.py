"""Qt GUI for MAGGIE."""

import os

# matplotlib's Qt backend prefers PyQt6 when several bindings are installed.
# Pin it to PySide6 before any ``backend_qtagg`` import in this package.
os.environ.setdefault("QT_API", "pyside6")
