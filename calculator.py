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
        self.equation = ""
        self.equals_was_previous = False
        self.operators = ["+","-","*","/"]
        self.decimal_was_clicked = False

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.ui.pushButton_0.clicked.connect(self.zero_clicked)
        self.ui.pushButton_1.clicked.connect(self.one_clicked)
        self.ui.pushButton_2.clicked.connect(self.two_clicked)
        self.ui.pushButton_3.clicked.connect(self.three_clicked)
        self.ui.pushButton_4.clicked.connect(self.four_clicked)
        self.ui.pushButton_5.clicked.connect(self.five_clicked)
        self.ui.pushButton_6.clicked.connect(self.six_clicked)
        self.ui.pushButton_7.clicked.connect(self.seven_clicked)
        self.ui.pushButton_8.clicked.connect(self.eight_clicked)
        self.ui.pushButton_9.clicked.connect(self.nine_clicked)
        self.ui.pushButton_decimal.clicked.connect(self.decimal_clicked)
        self.ui.pushButton_subtract.clicked.connect(self.subtract_clicked)
        self.ui.pushButton_divide.clicked.connect(self.divide_clicked)
        self.ui.pushButton_add.clicked.connect(self.add_clicked)
        self.ui.pushButton_multiply.clicked.connect(self.multiply_clicked)
        self.ui.pushButton_equal.clicked.connect(self.equals_clicked)
        self.ui.pushButton_delete.clicked.connect(self.delete_clicked)
        self.ui.pushButton_reset.clicked.connect(self.reset_clicked)
        self.ui.pushButton_left_bracket.clicked.connect(self.left_bracket_clicked)
        self.ui.pushButton_right_bracket.clicked.connect(self.right_bracket_clicked)        

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def zero_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            pass
        else:
            self.equation += "0"
            self.update_display()

    def one_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "1"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "1"
            self.update_display()
        else:
            self.equation += "1"
            self.update_display()
    
    def two_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "2"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "2"
            self.update_display()
        else:
            self.equation += "2"
            self.update_display()

    def three_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "3"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "3"
            self.update_display()
        else:
            self.equation += "3"
            self.update_display()

    def four_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "4"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "4"
            self.update_display()
        else:
            self.equation += "4"
            self.update_display()

    def five_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "5"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "5"
            self.update_display()
        else:
            self.equation += "5"
            self.update_display()

    def six_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "6"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "6"
            self.update_display()
        else:
            self.equation += "6"
            self.update_display()

    def seven_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "7"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "7"
            self.update_display()
        else:
            self.equation += "7"
            self.update_display()

    def eight_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "8"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "8"
            self.update_display()
        else:
            self.equation += "8"
            self.update_display()

    def nine_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation == "":
            self.equation += "9"
            self.update_display()
        elif self.equation[-1] == "0" and self.equation[-2] in self.operators:
            self.equation = self.equation[:-1]
            self.equation += "9"
            self.update_display()
        else:
            self.equation += "9"
            self.update_display()

    def decimal_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        if self.equation != "":
            if self.equation[-1] == ".":
                self.update_display()
        if self.decimal_was_clicked == False:
            self.equation += "."
            self.decimal_was_clicked = True
            self.update_display()

    def subtract_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        if self.equation != "":
            self.equation += "-"
            self.update_display()
        else:
            self.equation += "0-"
            self.update_display()

    def divide_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        if self.equation != "":
            if self.equation[-1] not in self.operators:
                self.equation += "/"
            self.update_display()
        else:
            self.equation += "0/"
            self.update_display()

    def add_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        if self.equation != "":
            if self.equation[-1] not in self.operators:
                self.equation += "+"
            self.update_display()
        else:
            self.equation += "0+"
            self.update_display()

    def multiply_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        if self.equation != "":
            if self.equation[-1] not in self.operators:
                self.equation += "*"
            self.update_display()
        else:
            self.equation += "0*"
            self.update_display()

    def equals_clicked(self):
        self.equals_was_previous = True
        self.decimal_was_clicked = False
        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            result = "Cannot Divide By Zero"
        except SyntaxError:
            result = "Invalid Syntax"
        self.equation = str(result)
        self.update_display()

    def delete_clicked(self):
        if self.equation != "":
            self.equals_was_previous = False
            if self.equation[-1] == ".":
                self.decimal_was_clicked = False
            self.equation = self.equation[:-1]
            self.update_display()

    def reset_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        self.equation = ""
        self.update_display()

    def left_bracket_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        self.equation += "("
        self.update_display()

    def right_bracket_clicked(self):
        self.equals_was_previous = False
        self.decimal_was_clicked = False
        self.equation += ")"
        self.update_display()

    # -- OTHER FUNCTIONS -- #
    def update_display(self):
        self.ui.label_display.setText(self.equation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
