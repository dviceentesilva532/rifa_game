# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(300, 433)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 433))
        MainWindow.setMaximumSize(QSize(300, 433))
        self.actionpagos = QAction(MainWindow)
        self.actionpagos.setObjectName(u"actionpagos")
        self.actiondeveno = QAction(MainWindow)
        self.actiondeveno.setObjectName(u"actiondeveno")
        self.actionlivre = QAction(MainWindow)
        self.actionlivre.setObjectName(u"actionlivre")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(300, 400))
        self.centralwidget.setMaximumSize(QSize(300, 400))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 301, 401))
        self.box = QVBoxLayout(self.verticalLayoutWidget)
        self.box.setObjectName(u"box")
        self.box.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.box.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 33))
        self.menupagos = QMenu(self.menubar)
        self.menupagos.setObjectName(u"menupagos")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menupagos.menuAction())
        self.menupagos.addAction(self.actionpagos)
        self.menupagos.addAction(self.actiondeveno)
        self.menupagos.addAction(self.actionlivre)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionpagos.setText(QCoreApplication.translate("MainWindow", u"pagos", None))
        self.actiondeveno.setText(QCoreApplication.translate("MainWindow", u"deveno", None))
        self.actionlivre.setText(QCoreApplication.translate("MainWindow", u"livre", None))
        self.menupagos.setTitle(QCoreApplication.translate("MainWindow", u"rifas", None))
    # retranslateUi

