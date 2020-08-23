import os
import sys

env_p = sys.prefix  # path to the env
print("Env. path: {}".format(env_p))

new_p = ''
for extra_p in (r"Library\mingw-w64\bin",
    r"Library\usr\bin",
    r"Library\bin",
    r"Scripts",
    r"bin"):
    new_p +=  os.path.join(env_p, extra_p) + ';'

os.environ["PATH"] = new_p + os.environ["PATH"]  # set it for Python

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QUrl
from mainwindow import Ui_MainWindow 
import sys, os
from shutil import copyfile
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import  QPalette, QColor


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.setWindowTitle("COVID-19 Data Visualizer")
        self.viewer = self.ui.webEngineView
        self.copyName = None            
        self.options = [self.ui.mapgraphbycases, self.ui.mapgraphbydeaths, self.ui.chartbycases, self.ui.chartbydeaths]
        
        self.ui.exportFigureSelection.triggered.connect(self.saveFile)        
        self.dataSelection()
            
        
    def dataSelection(self):
        for i in range(len(self.options)):
            self.checkDataSelection(i)
            
    def checkDataSelection(self, i):
        self.options[i].triggered.connect(lambda: self.displayData(str(self.options[i].text())))
                
    def displayData(self, text):
        filePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "Graphs/" + text + ".html"))
        self.copyName = os.path.basename(filePath)
        self.viewer.load(QUrl.fromLocalFile(filePath))
        
    def saveFile(self):
        savePath, _ = QFileDialog.getSaveFileName(self, "Save Figure As", "", "Hypertext Markup Language (*.html);;" "All files(*.*)")
        if(self.copyName != None and savePath != ''):
            copyPath = 'Graphs/' + self.copyName
            copyfile(copyPath, savePath)



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()

    app.setStyle("Fusion")

    # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 0, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    application.show()
    app.exec_()


if __name__ == "__main__":
    main()