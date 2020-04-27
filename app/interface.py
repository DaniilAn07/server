from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):

    # Styling Main Window
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(372, 645)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Vertical layout for the project
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # Setting Vertical layout name
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Viewing all messages in message_box
        self.message_box = QPlainTextEdit(self.centralwidget)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setReadOnly(True)

        # Adding message_box to main layout - vertical
        self.verticalLayout.addWidget(self.message_box)

        # Adding message input
        self.message_input = QLineEdit(self.centralwidget)
        self.message_input.setObjectName(u"message_input")

        # Adding message_input to main layout - vertical
        self.verticalLayout.addWidget(self.message_input)

        # Adding button
        self.message_button = QPushButton(self.centralwidget)
        self.message_button.setObjectName(u"message_button")

        # Adding message_button to main layout - vertical
        self.verticalLayout.addWidget(self.message_button)

        # Adding central widget to Main Window
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.message_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Connecting...", None))
        self.message_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your message here...", None))
        self.message_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi