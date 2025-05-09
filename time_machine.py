import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTime, QTimer, QUrl
from PyQt6.QtMultimedia import QSoundEffect

class Mainwindow(QMainWindow):
    def __init__(self):
        """
        Initialise the main window and set up the ui
        """
        super().__init__()
        uic.loadUi("time_machine.ui", self)
        self.show_time()

        # --- initialise variables
        self.clock_timer = QTimer()
        self.clock_timer.start(1000)

        self.sw_timer = QTimer()
        self.sw_time = QTime(0, 0, 0, 0)
        self.sw_running = False

        self.tm_timer = QTimer()
        self.tm_time = QTime(0, 0, 0)
        self.tm_running = False
        self.tm_alarm = QSoundEffect()
        self.tm_alarm.setSource(QUrl.fromLocalFile("alarm_sound.wav"))
        self.tm_alarm.setLoopCount(1)
        self.tm_alarm.setVolume(0.5)

        # --- connect signals to slots
        self.signals()

        # --- Initialise displays
        self.show_time()
        self.show_sw_time()
        self.show_tm_time()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        # clock
        self.clock_timer.timeout.connect(self.show_time)

        # stopwatch
        self.pushButton_sw_start.clicked.connect(self.start_sw)
        self.pushButton_sw_pause.clicked.connect(self.pause_sw)
        self.pushButton_sw_stop.clicked.connect(self.stop_sw)
        self.pushButton_sw_reset.clicked.connect(self.reset_sw)
        self.sw_timer.timeout.connect(self.update_sw)

        # timer
        self.pushButton_tm_start.clicked.connect(self.start_timer)
        self.pushButton_tm_pause.clicked.connect(self.pause_timer)
        self.pushButton_tm_stop.clicked.connect(self.stop_timer)
        self.pushButton_tm_reset.clicked.connect(self.reset_timer)
        self.tm_timer.timeout.connect(self.update_timer)
        
        # Add signal-slot connections here

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    # clock
    def show_time(self):
        """
        Update the clock display with the current time.
        """
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("h:mm:ssa")
        self.label_clock.setText(formatted_time)

    # stopwatch
    def show_sw_time(self):
        """
        Update the stopwatch display with the current stopwatch time
        """
        formatted_time = self.sw_time.toString("h:mm:ss:zz")
        self.label_stopwatch.setText(formatted_time)

    def start_sw(self):
        """
        start the stopwatch
        """
        self.sw_timer.start(100)
        self.sw_running = True

    def pause_sw(self):
        """
        pause the stopwatch
        """
        self.sw_running = not self.sw_running

    def stop_sw(self):
        """
        stop the stopwatch and reset the time
        """
        self.sw_running = False

    def reset_sw(self):
        """
        Reset the stopwatch time to zero
        """
        self.sw_time = QTime(0, 0, 0, 0)
        self.sw_running = False

    def update_sw(self):
        """
        Update the stopwatch time if it is running
        """
        if self.sw_running:
            self.sw_time = self.sw_time.addMSecs(100)
            self.show_sw_time()
    
    # timer
    def show_tm_time(self):
        """
        Update the timer display with the current time
        """
        formatted_time = self.tm_time.toString("h:mm:ss")
        self.label_tm_time.setText(formatted_time)

    def start_timer(self):
        """
        Start the timer with the time set from the spinboxes
        """
        self.tm_time = self.spinbox_to_time()
        self.tm_timer.start(1000)
        self.tm_running = True
        self.show_tm_time()

    def pause_timer(self):
        """
        Pause the timer
        """
        self.tm_running = not self.tm_running

    def stop_timer(self):
        """
        Stop the timer and reset the time
        """
        self.tm_running = False
        self.tm_time = QTime(0, 0, 0)
        self.show_tm_time()

    def reset_timer(self):
        """
        Reset the timer to the time in the spinboxes
        """
        self.tm_time = self.spinbox_to_time()
        self.show_tm_time()

    def update_timer(self):
        """
        Update the timer time if it is running
        """
        if self.tm_running:
            self.tm_time = self.tm_time.addSecs(-1)
            self.show_tm_time()
            if self.tm_time == QTime(0, 0, 0):
                self.tm_running = False
                self.tm_alarm.play()
    

    # Utilities
    def spinbox_to_time(self):
        """
        Convert the spinbox values to a QTime object
        """
        hours = self.spinBox_hours.value()
        minutes = self.spinBox_minutes.value()
        seconds = self.spinBox_seconds.value()
        return QTime(hours, minutes, seconds)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())