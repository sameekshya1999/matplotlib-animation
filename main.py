import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure
from itertools import count
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(110, 80, 541, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(310, 380, 160, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.startButton = QtWidgets.QPushButton(self.splitter)
        self.startButton.setStyleSheet("")
        self.startButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        layout = QVBoxLayout(self.graphicsView)
        self.dynamic_canvas = FigureCanvas(Figure(figsize=(10, 6)))
        layout.addWidget(self.dynamic_canvas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startButton.clicked.connect(self.animat)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))

    def __init__(self):
        self.i = count(step=0.25)
        self.x = []
        self.y = []

    def animat(self):
        self.num = next(self.i)

        self.dynamic_ax = self.dynamic_canvas.figure.subplots()
        x = np.linspace(-10, 10, 500)
        y = np.sin(x + time.time())

        self.line, = self.dynamic_ax.plot(x, y)
        self.timer = self.dynamic_canvas.new_timer(50)
        self.timer.add_callback(self.update_canvas)
        self.timer.start()
        self.pushButton_2.clicked.connect(self.stop_canvas)


    def update_canvas(self):
        x = np.linspace(-10, 10, 500)
        y = np.sin(x + time.time())
        self.line.set_data(x, y)
        self.line.figure.canvas.draw()

    def stop_canvas(self):
        self.timer.stop()


