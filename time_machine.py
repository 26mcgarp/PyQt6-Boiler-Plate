import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Mainwindow(QMainWindow):
    def __init__(self):
        """
        Initialise the main window and set up the ui
        """
        super().__init__()
        uic.loadUi("time_machine.ui", self)

        # --- initialise variables

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        pass # Add signal-slot connections here

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())