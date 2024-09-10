from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

from pytube import YouTube

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("MainUI.ui", self)

        self.pushButton.clicked.connect(self.DownloadVideo)

    def DownloadVideo(self):
        if self.radioButton.isChecked() == True:
            url = self.lineEdit.text()
            exit_path = self.lineEdit_2.text()
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            stream.download(output_path = exit_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    app.exec_()