# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(250, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(250, 150))
        MainWindow.setMaximumSize(QSize(250, 150))
        self.viewtable = QAction(MainWindow)
        self.viewtable.setObjectName(u"viewtable")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(60)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(250, 150))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 241, 123))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rifa = QComboBox(self.verticalLayoutWidget)
        self.rifa.setObjectName(u"rifa")
        sizePolicy.setHeightForWidth(self.rifa.sizePolicy().hasHeightForWidth())
        self.rifa.setSizePolicy(sizePolicy)
        self.rifa.setMinimumSize(QSize(135, 25))
        self.rifa.setMaximumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.rifa, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cliente = QLineEdit(self.verticalLayoutWidget)
        self.cliente.setObjectName(u"cliente")
        self.cliente.setMaximumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.cliente, 0, Qt.AlignmentFlag.AlignHCenter)

        self.botaosalva = QPushButton(self.verticalLayoutWidget)
        self.botaosalva.setObjectName(u"botaosalva")
        self.botaosalva.setMaximumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.botaosalva, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 250, 33))
        self.menutabela = QMenu(self.menubar)
        self.menutabela.setObjectName(u"menutabela")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menutabela.menuAction())
        self.menutabela.addAction(self.viewtable)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.viewtable.setText(QCoreApplication.translate("MainWindow", u"ver tabela", None))
        self.rifa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"numero do cliente", None))
        self.cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nome do cliente", None))
        self.botaosalva.setText(QCoreApplication.translate("MainWindow", u"salvar", None))
        self.menutabela.setTitle(QCoreApplication.translate("MainWindow", u"tabela", None))
    # retranslateUi

