from PyQt6.QtWidgets import *
from ddm import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def calculate(self):
        div0 = self.lineDiv0.text()
        yr1 = self.lineYr1.text()
        div1 = self.lineDiv1.text()
        yr2 = self.lineYr1_2.text()
        div2 = self.lineDiv1_2.text()
        yr3 = self.lineYr1_3.text()
        div3 = self.lineDiv1_3.text()
        CAPM = self.lineCAPM.text()
        Current_Market = self.lineCurrent.text()

        try:
            div0 = float(div0)

            if (len(div1)>0) and (len(yr1)>0):
                yr1 = int(yr1)
                div1 = float(div1)
            else:
                yr1, div1 = 0, 0
            if (len(div2) > 0) and (len(yr2) > 0):
                yr2 = int(yr2)
                div2 = float(div2)
            else:
                yr2, div2 = 0, 0
            if (len(div3) > 0) and (len(yr3) > 0):
                yr3 = int(yr3)
                div3 = float(div3)
            else:
                yr3, div3 = 0, 0

            CAPM = float(CAPM)*.01
            Current_Market = float(Current_Market)
            n = 0
            slope = 0

            if div3 == 0 :
                slope = (yr1 - yr2) / (div1 - div2)
            elif div3 != 0:
                slope = (yr1 - yr3) / (div1 - div3)

            if div1 != 0:
                n += 1
            if div2 != 0:
                n+= 1
            if div3 != 0:
                n+=1

            avg_div = (div1 + div2 + div3) / n
            growth_rate = slope/avg_div
            value = (div0*(1+growth_rate))/(CAPM - growth_rate)

            self.labelValue.setText((f'{value:.2f} vs <br/> Current Market {Current_Market}'))

            if value > Current_Market:
                self.labelOutput.setText('Under-Valued')
            else:
                self.labelOutput.setText('Over-Valued')

        except Exception as e :
            print(e)












