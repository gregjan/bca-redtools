# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redactwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RedactWindow(object):
    def setupUi(self, RedactWindow):
        RedactWindow.setObjectName("RedactWindow")
        RedactWindow.resize(594, 507)
        self.centralWidget = QtWidgets.QWidget(RedactWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.RedactTabs = QtWidgets.QTabWidget(self.centralWidget)
        self.RedactTabs.setObjectName("RedactTabs")
        self.RedactDiskImageTab = QtWidgets.QWidget()
        self.RedactDiskImageTab.setObjectName("RedactDiskImageTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.RedactDiskImageTab)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SelectConfigLabel = QtWidgets.QLabel(self.RedactDiskImageTab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SelectConfigLabel.setFont(font)
        self.SelectConfigLabel.setObjectName("SelectConfigLabel")
        self.gridLayout_2.addWidget(self.SelectConfigLabel, 0, 0, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.RedactDiskImageTab)
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_2.addWidget(self.CloseButton, 4, 2, 1, 1)
        self.RedactionProgress = QtWidgets.QProgressBar(self.RedactDiskImageTab)
        self.RedactionProgress.setMaximum(1)
        self.RedactionProgress.setProperty("value", 0)
        self.RedactionProgress.setTextVisible(False)
        self.RedactionProgress.setObjectName("RedactionProgress")
        self.gridLayout_2.addWidget(self.RedactionProgress, 4, 0, 1, 1)
        self.ProgressLabel = QtWidgets.QLabel(self.RedactDiskImageTab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ProgressLabel.setFont(font)
        self.ProgressLabel.setObjectName("ProgressLabel")
        self.gridLayout_2.addWidget(self.ProgressLabel, 2, 0, 1, 1)
        self.SelectConfigEdit = QtWidgets.QLineEdit(self.RedactDiskImageTab)
        self.SelectConfigEdit.setObjectName("SelectConfigEdit")
        self.gridLayout_2.addWidget(self.SelectConfigEdit, 1, 0, 1, 6)
        self.SelectConfigTool = QtWidgets.QToolButton(self.RedactDiskImageTab)
        self.SelectConfigTool.setObjectName("SelectConfigTool")
        self.gridLayout_2.addWidget(self.SelectConfigTool, 1, 6, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.RedactDiskImageTab)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 3, 0, 1, 6)
        self.RunButton = QtWidgets.QPushButton(self.RedactDiskImageTab)
        self.RunButton.setObjectName("RunButton")
        self.gridLayout_2.addWidget(self.RunButton, 4, 4, 1, 1)
        self.CancelButton = QtWidgets.QPushButton(self.RedactDiskImageTab)
        self.CancelButton.setObjectName("CancelButton")
        self.gridLayout_2.addWidget(self.CancelButton, 4, 3, 1, 1)
        self.RedactTabs.addTab(self.RedactDiskImageTab, "")
        self.EditConfigTab = QtWidgets.QWidget()
        self.EditConfigTab.setObjectName("EditConfigTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.EditConfigTab)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.EditConfigLabel = QtWidgets.QLabel(self.EditConfigTab)
        self.EditConfigLabel.setObjectName("EditConfigLabel")
        self.gridLayout_3.addWidget(self.EditConfigLabel, 0, 0, 1, 2)
        self.LoadButton = QtWidgets.QPushButton(self.EditConfigTab)
        self.LoadButton.setObjectName("LoadButton")
        self.gridLayout_3.addWidget(self.LoadButton, 2, 0, 1, 1)
        self.SaveButton = QtWidgets.QPushButton(self.EditConfigTab)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout_3.addWidget(self.SaveButton, 2, 1, 1, 1)
        self.EditConfigText = QtWidgets.QTextEdit(self.EditConfigTab)
        self.EditConfigText.setObjectName("EditConfigText")
        self.gridLayout_3.addWidget(self.EditConfigText, 1, 0, 1, 2)
        self.RedactTabs.addTab(self.EditConfigTab, "")
        self.gridLayout.addWidget(self.RedactTabs, 0, 0, 1, 1)
        RedactWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(RedactWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 594, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        RedactWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(RedactWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        RedactWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(RedactWindow)
        self.statusBar.setObjectName("statusBar")
        RedactWindow.setStatusBar(self.statusBar)
        self.actionCopy = QtWidgets.QAction(RedactWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(RedactWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(RedactWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionExit = QtWidgets.QAction(RedactWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_bca_redtools = QtWidgets.QAction(RedactWindow)
        self.actionAbout_bca_redtools.setObjectName("actionAbout_bca_redtools")
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout_bca_redtools)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RedactWindow)
        self.RedactTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RedactWindow)

    def retranslateUi(self, RedactWindow):
        _translate = QtCore.QCoreApplication.translate
        RedactWindow.setWindowTitle(_translate("RedactWindow", "Disk Image Redaction"))
        self.SelectConfigLabel.setText(_translate("RedactWindow", "Select a configuration file"))
        self.CloseButton.setText(_translate("RedactWindow", "Close"))
        self.ProgressLabel.setText(_translate("RedactWindow", "Progress (console output)"))
        self.SelectConfigEdit.setPlaceholderText(_translate("RedactWindow", "/path/to/config/file"))
        self.SelectConfigTool.setText(_translate("RedactWindow", "..."))
        self.RunButton.setText(_translate("RedactWindow", "Run"))
        self.CancelButton.setText(_translate("RedactWindow", "Cancel"))
        self.RedactTabs.setTabText(self.RedactTabs.indexOf(self.RedactDiskImageTab), _translate("RedactWindow", "Redact Disk Image"))
        self.EditConfigLabel.setText(_translate("RedactWindow", "Load, edit, and save (or create a new configuration) using the form below."))
        self.LoadButton.setText(_translate("RedactWindow", "Load"))
        self.SaveButton.setText(_translate("RedactWindow", "Save"))
        self.RedactTabs.setTabText(self.RedactTabs.indexOf(self.EditConfigTab), _translate("RedactWindow", "Edit Configuration"))
        self.menuFile.setTitle(_translate("RedactWindow", "File"))
        self.menuEdit.setTitle(_translate("RedactWindow", "Edit"))
        self.menuHelp.setTitle(_translate("RedactWindow", "Help"))
        self.actionCopy.setText(_translate("RedactWindow", "Copy"))
        self.actionPaste.setText(_translate("RedactWindow", "Paste"))
        self.actionCut.setText(_translate("RedactWindow", "Cut"))
        self.actionExit.setText(_translate("RedactWindow", "Exit"))
        self.actionAbout_bca_redtools.setText(_translate("RedactWindow", "About bca-redtools"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RedactWindow = QtWidgets.QMainWindow()
    ui = Ui_RedactWindow()
    ui.setupUi(RedactWindow)
    RedactWindow.show()
    sys.exit(app.exec_())

