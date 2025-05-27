import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime, QUrl
from PyQt6.QtMultimedia import QSoundEffect

# connect new values dialog

class NewValues(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("change values.ui", self)
        self.parent = parent
        self.spinBox_hours.setRange(0, 23)
        self.spinBox_minutes.setRange(0, 59)
        self.spinBox_seconds.setRange(0, 59)
        self.spinBox_score1.setRange(-99, 99)
        self.spinBox_score2.setRange(-99, 99)
        self.spinBox_score3.setRange(-99, 99)

    def set_for_edit(self):
        self.lineEdit_team1_name.setText(self.parent.label_team1_name.text())
        self.lineEdit_team2_name.setText(self.parent.label_team2_name.text())
        self.spinBox_hours.setValue(self.parent.hours)
        self.spinBox_minutes.setValue(self.parent.minutes)
        self.spinBox_seconds.setValue(self.parent.seconds)
        self.spinBox_score1.setValue(self.parent.score1)
        self.spinBox_score2.setValue(self.parent.score2)
        self.spinBox_score3.setValue(self.parent.score3)
        
    def get_values(self):
        self.data = {
            "team1_name": self.lineEdit_team1_name.text(),
            "team2_name": self.lineEdit_team2_name.text(),
            "hours": self.spinBox_hours.value(),
            "minutes": self.spinBox_minutes.value(),
            "seconds": self.spinBox_seconds.value(),
            "score1": self.spinBox_score1.value(),
            "score2": self.spinBox_score2.value(),
            "score3": self.spinBox_score3.value(),
            "team1_score": 0,
            "team2_score": 0
        }
        return self.data
    

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
        self.actionSave_2.triggered.connect(self.save_scoreboard)
        self.actionOpen.triggered.connect(self.open_scoreboard)
        self.actionNew.triggered.connect(self.open_dialoge)
        self.actionEdit.triggered.connect(self.edit_values)
        self.pushButton_team1_score1.clicked.connect(self.add_score)
        self.pushButton_team2_score1.clicked.connect(self.add_score)
        self.pushButton_team1_score2.clicked.connect(self.add_score)
        self.pushButton_team2_score2.clicked.connect(self.add_score)
        self.pushButton_team1_score3.clicked.connect(self.add_score)
        self.pushButton_team2_score3.clicked.connect(self.add_score)
        self.pushButton_reset_team1.clicked.connect(self.reset_team1_score)
        self.pushButton_reset_team2.clicked.connect(self.reset_team2_score)
        self.pushButton_reset_all.clicked.connect(self.reset_scores)

        # check file status
        self.file = False
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self.update_button_status)
        self.status_timer.start(100)

        # score
        self.team1_score = 0
        self.team2_score = 0
        self.label_team1_score.setText(str(self.team1_score))
        self.label_team2_score.setText(str(self.team2_score))

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        pass  # Add signal-slot connections here, e.g., button.clicked.connect(self.some_function) 

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def update_button_status(self):
        if not self.file:
            self.button_status = False
        else:
            self.button_status = True
        self.change_button_status(self.button_status)
    
    def change_button_status(self, button_status):
        self.pushButton_start.setEnabled(self.button_status)
        self.pushButton_pause.setEnabled(self.button_status)
        self.pushButton_reset.setEnabled(self.button_status)
        self.pushButton_team1_score1.setEnabled(self.button_status)
        self.pushButton_team2_score1.setEnabled(self.button_status)
        self.pushButton_team1_score2.setEnabled(self.button_status)
        self.pushButton_team2_score2.setEnabled(self.button_status)
        self.pushButton_team1_score3.setEnabled(self.button_status)
        self.pushButton_team2_score3.setEnabled(self.button_status)
        self.label_error.setHidden(self.button_status)
        self.actionEdit.setEnabled(self.button_status)
        self.actionSave_2.setEnabled(self.button_status)
        self.pushButton_reset_team1.setEnabled(self.button_status)
        self.pushButton_reset_team2.setEnabled(self.button_status)
        self.pushButton_reset_all.setEnabled(self.button_status)

    # timer
    def show_time(self):
        formatted_time = self.time.toString("h:mm:ss")
        self.label_timer.setText(formatted_time)

    def start_timer(self):
        #self.time = QTime(self.hours, self.minutes, self.seconds)
        self.timer.start(1000)
        self.running = True
        self.show_time()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.time = QTime(self.hours, self.minutes, self.seconds)
        self.show_time()
        self.running = False

    def update_timer(self):
        if self.running:
            self.time = self.time.addSecs(-1)
            self.show_time()
            if self.time == QTime(0, 0, 0):
                self.running = False
                self.alarm.play()
    
    # new values
    def save_scoreboard(self):
        self.data = {
            "team1_name": self.label_team1_name.text(),
            "team2_name": self.label_team2_name.text(),
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
            "score1": self.score1,
            "score2": self.score2,
            "score3": self.score3,
            "team1_score": self.team1_score,
            "team2_score": self.team2_score
        }
        suggested_file_name = f"{self.data["team1_name"]}_vs_{self.data["team2_name"]}.json"
        file_path, _= QFileDialog.getSaveFileName(self,
                                                "Save Scoreboard Values",
                                                suggested_file_name,
                                                "JSON Files(*.json)")
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.data, f, indent=4)

    def open_scoreboard(self):
        file_path, _= QFileDialog.getOpenFileName(self,
                                                  "Open Scoreboard Values",
                                                  "",
                                                  "JSON Files(*.json)")
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)
                self.set_values(data)

    def open_dialoge(self):
        dialog = NewValues(self)
        if dialog.exec():
            data = dialog.get_values()
            self.set_values(data)

    def edit_values(self):
        dialog = NewValues(self)
        dialog.set_for_edit()
        if dialog.exec():
            data = dialog.get_values()
            self.set_values(data)

    def set_values(self, data):
        self.label_team1_name.setText(data["team1_name"])
        self.label_team2_name.setText(data["team2_name"])
        self.score1 = data["score1"]
        self.score2 = data["score2"]
        self.score3 = data["score3"]
        self.pushButton_team1_score1.setText(str(self.score1))
        self.pushButton_team2_score1.setText(str(self.score1))
        self.pushButton_team1_score2.setText(str(self.score2))
        self.pushButton_team2_score2.setText(str(self.score2))
        self.pushButton_team1_score3.setText(str(self.score3))
        self.pushButton_team2_score3.setText(str(self.score3))
        self.time = QTime(data["hours"], data["minutes"], data["seconds"])
        self.hours = data["hours"]
        self.minutes = data["minutes"]
        self.seconds = data["seconds"]
        self.team1_score = data["team1_score"]
        self.team2_score = data["team2_score"]
        self.show_time()
        self.file = True

    # scoring
    def add_score(self):
        sender = self.sender()
        if sender == self.pushButton_team1_score1:
            self.team1_score += self.score1
        elif sender == self.pushButton_team1_score2:
            self.team1_score += self.score2
        elif sender == self.pushButton_team1_score3:
            self.team1_score += self.score3
        elif sender == self.pushButton_team2_score1:
            self.team2_score += self.score1
        elif sender == self.pushButton_team2_score2:
            self.team2_score += self.score2
        elif sender == self.pushButton_team2_score3:
            self.team2_score += self.score3
        self.label_team1_score.setText(str(self.team1_score))
        self.label_team2_score.setText(str(self.team2_score))

    def reset_scores(self):
        self.team1_score = 0
        self.team2_score = 0
        self.label_team1_score.setText(str(self.team1_score))
        self.label_team2_score.setText(str(self.team2_score))
    
    def reset_team1_score(self):
        self.team1_score = 0
        self.label_team1_score.setText(str(self.team1_score))
    
    def reset_team2_score(self):
        self.team2_score = 0
        self.label_team2_score.setText(str(self.team2_score))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())