# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shafttTbrqA.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(365, 452)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.shaft_box = QWidget()
        self.shaft_box.setObjectName(u"shaft_box")
        self.shaft_box.setGeometry(QRect(0, 0, 347, 374))
        self.verticalLayout_2 = QVBoxLayout(self.shaft_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.shaft_H_line_edit = QLineEdit(self.shaft_box)
        self.shaft_H_line_edit.setObjectName(u"shaft_H_line_edit")

        self.verticalLayout_2.addWidget(self.shaft_H_line_edit)

        self.frame_2 = QFrame(self.shaft_box)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.shaft_clear_button = QPushButton(self.frame_2)
        self.shaft_clear_button.setObjectName(u"shaft_clear_button")

        self.horizontalLayout_2.addWidget(self.shaft_clear_button)

        self.shaft_calc_button = QPushButton(self.frame_2)
        self.shaft_calc_button.setObjectName(u"shaft_calc_button")

        self.horizontalLayout_2.addWidget(self.shaft_calc_button)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.shaft_box)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.shaft_table_source = QTableWidget(self.frame)
        if (self.shaft_table_source.columnCount() < 1):
            self.shaft_table_source.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.shaft_table_source.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.shaft_table_source.rowCount() < 1):
            self.shaft_table_source.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.shaft_table_source.setVerticalHeaderItem(0, __qtablewidgetitem1)
        self.shaft_table_source.setObjectName(u"shaft_table_source")
        self.shaft_table_source.horizontalHeader().setVisible(False)
        self.shaft_table_source.horizontalHeader().setStretchLastSection(True)
        self.shaft_table_source.verticalHeader().setVisible(True)
        self.shaft_table_source.verticalHeader().setHighlightSections(True)

        self.horizontalLayout.addWidget(self.shaft_table_source)

        self.shaft_table_result = QTableWidget(self.frame)
        if (self.shaft_table_result.columnCount() < 1):
            self.shaft_table_result.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.shaft_table_result.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        if (self.shaft_table_result.rowCount() < 1):
            self.shaft_table_result.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.shaft_table_result.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.shaft_table_result.setObjectName(u"shaft_table_result")
        self.shaft_table_result.horizontalHeader().setVisible(False)
        self.shaft_table_result.horizontalHeader().setCascadingSectionResizes(False)
        self.shaft_table_result.horizontalHeader().setDefaultSectionSize(100)
        self.shaft_table_result.horizontalHeader().setHighlightSections(True)
        self.shaft_table_result.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.shaft_table_result)


        self.verticalLayout_2.addWidget(self.frame)

        self.shaft_history_button = QPushButton(self.shaft_box)
        self.shaft_history_button.setObjectName(u"shaft_history_button")

        self.verticalLayout_2.addWidget(self.shaft_history_button)

        self.toolBox.addItem(self.shaft_box, u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043c\u0435\u0442\u043e\u043a \u0442\u0440\u0443\u0431 \u0432 \u043a\u043e\u043b\u043e\u0434\u0446\u0435")
        self.tk_box = QWidget()
        self.tk_box.setObjectName(u"tk_box")
        self.tk_box.setGeometry(QRect(0, 0, 347, 374))
        self.toolBox.addItem(self.tk_box, u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043c\u0435\u0442\u043e\u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0442\u0435\u043f\u043b\u043e\u043a\u0430\u043c\u0435\u0440\u044b")

        self.verticalLayout.addWidget(self.toolBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Shaft calculator", None))
        self.shaft_clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.shaft_calc_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        ___qtablewidgetitem = self.shaft_table_source.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem1 = self.shaft_table_result.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0435\u0432\u044b\u0448\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.shaft_table_result.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.shaft_history_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.shaft_box), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043c\u0435\u0442\u043e\u043a \u0442\u0440\u0443\u0431 \u0432 \u043a\u043e\u043b\u043e\u0434\u0446\u0435", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tk_box), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043c\u0435\u0442\u043e\u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0442\u0435\u043f\u043b\u043e\u043a\u0430\u043c\u0435\u0440\u044b", None))
    # retranslateUi

