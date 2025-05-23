import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime, QUrl
from PyQt6.QtMultimedia import QSoundEffect

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("Scoreboard.ui", self)
        # --- initialise variables
        # timer
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.running = False
        self.show_time()

        # alarm
        self.alarm = QSoundEffect()
        self.alarm.setSource(QUrl.fromLocalFile("alarm_sound.wav"))
        self.alarm.setLoopCount(1)
        self.alarm.setVolume(0.5)

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
    # timer
    def show_time(self):
        formatted_time = self.time.toString("h:mm:ss")
        self.label_timer.setText(formatted_time)

    def start_timer(self):
        self.time = QTime(self.hours, self.minutes, self.seconds)
        self.timer.start(1000)
        self.running = True
        self.show_time()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.time = QTime(self.hours, self.minutes, self.seconds)
        self.show_time()

    def update_timer(self):
        if self.running:
            self.time = self.time.addSecs(-1)
            self.show_time()
            if self.time == QTime(0, 0, 0):
                self.running = False
                self.alarm.play()
    
    # new values
    def save_new_scoreboard(self):
        self.team1_name = self.lineEdit_team1_name.text()
        self.team2_name = self.lineEdit_team2_name.text()
        self.hours = self.spinBox_hours.value()
        self.minutes = self.spinBox_minutes.value()
        self.seconds = self.spinBox_seconds.value()
        if self.radioButton_score1_subtract.toggled():
            self.score1 = self.spinBox_score1.value()*-1
        elif self.radioButton_score1_add.toggled():
            self.score1 = self.spinBox_score1.value()
        elif self.radioButton_score2_subtract.toggled():
            self.score2 = self.spinBox_score2.value()*-1
        elif self.radioButton_score2_add.toggled():
            self.score2 = self.spinBox_score2.value()
        elif self.radioButton_score3_subtract.toggled():
            self.score3 = self.spinBox_score3.value()*-1
        elif self.radioButton_score3_add.toggled():
            self.score3 = self.spinBox_score3.value()
        self.data = {
            "team1_name": self.team1_name,
            "team2_name": self.team2_name,
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
            "score1": self.score1,
            "score2": self.score2,
            "score3": self.score3
        }
        suggested_file_name = f"{self.team1_name}_vs_{self.team2_name}.json"
        file_path = QFileDialog.getSaveFileName(self,
                                                "Save Scoreboard Values",
                                                suggested_file_name,
                                                "JSON Files(*.json)")
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.data, f, indent=4)
    
    # score buttons
    '''
    def get_score_values(self):
        self.score1 = self.spinBox_score1.value()
        if self.radioButton_score1_subtract.toggled:
            self.score1 = self.score1*-1
        print(self.score1)
        self.score2 = self.spinBox_score2.value()
        if self.radioButton_score2_subtract.toggled:
            self.score2 = self.score2*-1
        print(self.score2)
        self.score3 = self.spinBox_score3.value()
        if self.radioButton_score3_subtract.toggled:
            self.score3 = self.score3*-1
        print(self.score3)

    def update_score_buttons(self):
        self.get_score_values()
        self.pushButton_team1_score1.text = self.score1
        self.pushButton_team2_score1.text = self.score1
        self.pushButton_team1_score2.text = self.score2
        self.pushButton_team2_score2.text = self.score2
        self.pushButton_team1_score3.text = self.score3
        self.pushButton_team2_score3.text = self.score3
        print(self.pushButton_team2_score3.text)
        print(self.spinBox_score3.value())
        '''
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
