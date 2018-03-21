# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\���ٽ�վ\ok.ui'
#
# Created: Sat Jun 27 00:32:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 250, 351, 33))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hboxlayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(71, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.layoutWidget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.okButton.setText(_translate("Dialog", "&确定", None))
        self.cancelButton.setText(_translate("Dialog", "&取消", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

