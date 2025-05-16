import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- initialise variables

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.ui.pushButton.clicked.connect(self.button_clicked)

    # ---- SLOTS ---- #
    def button_clicked(self):
        self.ui.label_2.setText("I'm clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
