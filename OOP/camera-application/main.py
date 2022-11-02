"""
    My first camera application

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2


class Window(QWidget):
    camera_icon = './cam.png'
    """ Main App Window """

    def __init__(self):
        super().__init__()

        # variables for the camera window
        self.window_width = 640
        self.window_height = 480

        # setup the window
        self.setWindowTitle("Camera Application")
        self.setFixedSize(self.window_width, self.window_height)
        self.setGeometry(0, 0, self.window_width, self.window_height)
        self.ui()

        # setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        # Load Icon
        self.camera_icon = QIcon(camera_icon)

    def ui(self):
        """ Contains the UI elements """

        # layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Image Label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.window_width,
                                     self.window_height)

        # capture Button
        self.capture_button = QPushButton(self)
        self.capture_button.setIcon(self.camera_icon)
        self.capture_button.setStyleSheet(
            "border: 2px solid black; border-radius: 10px;")
        self.capture_button.setFixedSize(50, 50)
        self.capture_button.clicked.connect(self.save_image)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        grid.addWidget(self.capture_button, 0, 0)
        grid.addWidget(self.image_label, 0, 1)

        self.show()

    def update(self):
        """ Update the camera window """
        _, self.frame = self.cap.read()

        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width
        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)

        self.image_label.setPixmap(QPixmap.fromImage(q_frame))

    def save_image(self):
        """ Save the image to the disk """
        pass

    def record(self):
        """ Record the video """
        pass


app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
