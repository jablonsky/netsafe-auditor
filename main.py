import sys

from PyQt6.QtGui import QColor, QIcon, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QMainWindow,
    QStyleFactory,
)
from PyQt6.uic import loadUi

from utils.paths import resource_path


# UI resources loaded by the application.
MAIN_WINDOW = resource_path("ui", "designer", "main.ui")
WINDOW_ICON = resource_path("ui", "designer", "icons", "shield.png")


def configure_fusion_style(app):
    """Apply a predictable dark Fusion style on every desktop platform."""
    fusion_style = QStyleFactory.create("Fusion")
    if fusion_style is None:
        raise RuntimeError("The required Qt Fusion style is not available.")

    app.setStyle(fusion_style)

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(160, 160, 160))

    disabled = QPalette.ColorGroup.Disabled
    palette.setColor(disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
    palette.setColor(disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
    palette.setColor(disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
    palette.setColor(disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))
    palette.setColor(
        disabled,
        QPalette.ColorRole.HighlightedText,
        QColor(127, 127, 127),
    )

    app.setPalette(palette)


class MainWindow(QMainWindow):
    """Main application window and basic UI navigation."""

    def __init__(self):
        super().__init__()

        loadUi(str(MAIN_WINDOW), self)
        self.setWindowIcon(QIcon(str(WINDOW_ICON)))
        self.resize(1100, 700)

        self._configure_navigation()
        self._configure_inactive_actions()

        self.action_Exit.triggered.connect(self.close)
        self.statusbar.showMessage("Ready — no device connected")

    def _configure_navigation(self):
        """Connect the available sidebar buttons to their application pages."""
        self.navigation_group = QButtonGroup(self)
        self.navigation_group.setExclusive(True)

        available_pages = (
            (self.pushButton_dashboard, self.page_dashboard),
            (self.pushButton_devices, self.page_devices),
        )

        for button, page in available_pages:
            button.setCheckable(True)
            button.setProperty("navigation", True)
            button.clicked.connect(
                lambda _checked, target=page: self.stackedWidget.setCurrentWidget(target)
            )
            self.navigation_group.addButton(button)

        self.pushButton_dashboard.setChecked(True)
        self.stackedWidget.setCurrentWidget(self.page_dashboard)

        self.setStyleSheet(
            """
            QPushButton[navigation="true"]:checked {
                background-color: #2563eb;
                color: white;
                font-weight: 600;
            }
            QPushButton[navigation="true"]:disabled {
                color: #808080;
            }
            """
        )

    def _configure_inactive_actions(self):
        """Mark controls that will be implemented in later learning steps."""
        coming_later = (
            self.pushButton_audit,
            self.pushButton_reports,
            self.pushButton_settings,
            self.button_test_connection,
            self.button_save_device,
            self.button_disconnect,
        )

        for button in coming_later:
            button.setEnabled(False)
            button.setToolTip("Planned for a later development step")


def main():
    """Start NetSafe Auditor and return the Qt exit code."""
    app = QApplication(sys.argv)
    configure_fusion_style(app)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
