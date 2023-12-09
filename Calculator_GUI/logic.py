from PyQt6.QtWidgets import *
from calculator import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def submit(self: None) -> None:
        """ perform calculations """
        screen = self.labelOutput.text()
        try:
            answer = eval(screen)
            self.labelOutput.setText(str(answer))
        except:
            self.labelOutput.setText("Error")

    def press(self, pressed: type(None)) -> None:
        """ user input data"""
        if pressed == 'C':
            self.labelOutput.setText('')
        else:
            self.labelOutput.setText(f'{self.labelOutput.text()}{pressed}')

    def decimal(self: None) -> None:
        """ Adds decimal point"""
        screen = self.labelOutput.text()
        if '.' in screen:
            pass
        else:
            self.labelOutput.setText(f'{screen}.')

    def negative(self: None) -> None:
        """Turns value negative"""
        screen = self.labelOutput.text()
        if '-' in screen:
            self.labelOutput.setText(screen.replace('-',''))
        else:
            self.labelOutput.setText(f'-{screen}')

