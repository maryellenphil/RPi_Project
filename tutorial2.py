from PyQt5 import QtCore, QtGui, QtWidgets
'''USER CODE'''
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
led=LED(23)

led_pin=23
GPIO.setup(led_pin, GPIO.OUT)
pwm=GPIO.PWM(led_pin,100)
pwm.start(100)

def ledToggle():
    if led.is_lit:
        led.off()
    else:
        led.on()
'''USER CODE'''



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 70, 251, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)

        ''' USER CODE'''
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        '''USER CODE'''

        self.verticalSlider.setGeometry(QtCore.QRect(40, 30, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 71, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "On/Off"))
        self.label.setText(_translate("MainWindow", "Brightness"))
        '''USER CODE'''
        self.pushButton.clicked.connect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)

    def sliderMov(self):
        value=self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
        '''USER CODE'''

'''USER CODE'''
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
'''USER CODE'''
