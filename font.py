from PyQt5 import QtGui

mainFont = "Arial Rounded MT Bold"

label_font = QtGui.QFont()
label_font.setFamily(mainFont)
label_font.setPointSize(16)
label_font.setBold(True)
label_font.setWeight(75)

button_font = QtGui.QFont()
button_font.setFamily(mainFont)
button_font.setPointSize(12)
button_font.setBold(True)
button_font.setWeight(75)

input_font = QtGui.QFont()
input_font.setPointSize(34)
input_font.setBold(True)
input_font.setWeight(75)