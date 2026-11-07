"""Application entry point.

Launch with the installed ``maggie`` command or ``python -m maggie``.
"""

from __future__ import annotations

import sys


def main() -> int:
    # Import Qt lazily so importing this module (e.g. for ``--help`` tooling or
    # tests) doesn't require a display.
    from PySide6.QtWidgets import QApplication

    from maggie.gui.start_page import StartPage
    from maggie.gui.theme import apply_theme

    app = QApplication(sys.argv[:1])
    apply_theme(app)
    window = StartPage()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
