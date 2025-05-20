import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("scoreboard.ui", self)
        # --- initialise variables
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.running = False
        self.show_time()

        # --- connect signals to slots 
        self.signals()
        self.pushButton_start.clicked.connect(self.start_timer)
        self.pushButton_pause.clicked.connect(self.pause_timer)
        self.pushButton_reset.clicked.connect(self.reset_timer)
        self.timer.timeout.connect(self.update_timer)

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        pass  # Add signal-slot connections here, e.g., button.clicked.connect(self.some_function) 

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def show_time(self):
        formatted_time = self.time.toString("h:mm:ss")
        self.label_timer.setText(formatted_time)

    def start_timer(self):
        self.time = self.spinbox_to_time()
        self.timer.start(1000)
        self.running = True
        self.show_time()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.time = self.spinbox_to_time()
        self.show_time()

    def update_timer(self):
        if self.running:
            self.time = self.time.addSecs(-1)
            self.show_time()
            if self.time == QTime(0, 0, 0):
                self.running = False
    
    def spinbox_to_time(self):
        hours = self.spinBox_hours.value()
        minutes = self.spinBox_minutes.value()
        seconds = self.spinBox_seconds.value()
        return QTime(hours, minutes, seconds)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
