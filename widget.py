from PyQt5 import QtCore, QtGui, QtWidgets
import re
import datetime as dt
from style_sheet import *
from geometry import *
from font import *


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(670, 340)
        widget.setMaximumSize(widget_geometry)
        widget.setStyleSheet(widgetStyle)

        self.dubai_label = QtWidgets.QLabel(widget)
        self.dubai_label.setGeometry(dubai_label_geometry)
        self.dubai_label.setFont(label_font)
        self.dubai_label.setObjectName("dubai_label")
        self.gmt_label = QtWidgets.QLabel(widget)
        self.gmt_label.setGeometry(gmt_label_geometry)
        self.gmt_label.setFont(label_font)
        self.gmt_label.setObjectName("gmt_label")

        self.convert_button = QtWidgets.QPushButton(widget)
        self.convert_button.setGeometry(button_geometry)
        self.convert_button.setFont(button_font)
        self.convert_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.convert_button.setStyleSheet(buttonStyle)
        self.convert_button.setObjectName("convert_button")

        self.dubai_input = QtWidgets.QTextEdit(widget)
        self.dubai_input.setGeometry(dubai_input_geometry)
        self.dubai_input.setFont(input_font)
        self.dubai_input.setStyleSheet(inputStyle)
        self.dubai_input.setObjectName("dubai_input")

        self.gmt_input = QtWidgets.QTextEdit(widget)
        self.gmt_input.setGeometry(gmt_input_geometry)
        self.gmt_input.setFont(input_font)
        self.gmt_input.setStyleSheet(inputStyle)
        self.gmt_input.setObjectName("gmt_input")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        widget.setTabOrder(self.dubai_input, self.gmt_input)
        widget.setTabOrder(self.gmt_input, self.convert_button)

    def clickCallback(self):
        gmt_text = re.sub("[^0-9:]", "", self.gmt_input.toPlainText())
        dubai_text = re.sub("[^0-9:]", "", self.dubai_input.toPlainText())
        if dubai_text != "":
            try:
                converted_time = dt.datetime.strptime(dubai_text, '%H:%M') + dt.timedelta(hours=-4)
                converted_time = dt.datetime.strftime(converted_time, "%H:%M")
                self.gmt_input.setText(converted_time)
            except:
                pass
        elif gmt_text != "":
            try:
                converted_time = dt.datetime.strptime(gmt_text, '%H:%M') + dt.timedelta(hours=4)
                converted_time = dt.datetime.strftime(converted_time, "%H:%M")
                self.dubai_input.setText(converted_time)
            except:
                pass

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Dubai to GMT converter"))
        self.dubai_label.setToolTip(_translate("widget", "<html><head/><body><p><br/></p></body></html>"))
        self.dubai_label.setText(_translate("widget", "DUBAI TIME"))
        self.gmt_label.setToolTip(_translate("widget", "<html><head/><body><p><br/></p></body></html>"))
        self.gmt_label.setText(_translate("widget", "GMT"))
        self.convert_button.setText(_translate("widget", "Convert"))
        self.convert_button.clicked.connect(self.clickCallback)
