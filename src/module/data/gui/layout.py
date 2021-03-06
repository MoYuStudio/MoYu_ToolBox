# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\module\data\gui\layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(718, 318)
        Window.setStyleSheet("")
        self.gridLayout_6 = QtWidgets.QGridLayout(Window)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(Window)
        self.tabWidget.setMinimumSize(QtCore.QSize(700, 300))
        self.tabWidget.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget_hub = QtWidgets.QWidget()
        self.tabWidget_hub.setObjectName("tabWidget_hub")
        self.tabWidget.addTab(self.tabWidget_hub, "")
        self.tabWidget_up = QtWidgets.QWidget()
        self.tabWidget_up.setObjectName("tabWidget_up")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabWidget_up)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_obs = QtWidgets.QPushButton(self.tabWidget_up)
        self.pushButton_obs.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_obs.setObjectName("pushButton_obs")
        self.gridLayout_4.addWidget(self.pushButton_obs, 0, 0, 1, 1)
        self.pushButton_androidtopc = QtWidgets.QPushButton(self.tabWidget_up)
        self.pushButton_androidtopc.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_androidtopc.setObjectName("pushButton_androidtopc")
        self.gridLayout_4.addWidget(self.pushButton_androidtopc, 2, 0, 1, 1)
        self.pushButton_liveass = QtWidgets.QPushButton(self.tabWidget_up)
        self.pushButton_liveass.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_liveass.setObjectName("pushButton_liveass")
        self.gridLayout_4.addWidget(self.pushButton_liveass, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidget_up, "")
        self.tabWidget_mc = QtWidgets.QWidget()
        self.tabWidget_mc.setObjectName("tabWidget_mc")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabWidget_mc)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_mcserver_v = QtWidgets.QPushButton(self.tabWidget_mc)
        self.pushButton_mcserver_v.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_v.setAutoDefault(False)
        self.pushButton_mcserver_v.setDefault(False)
        self.pushButton_mcserver_v.setObjectName("pushButton_mcserver_v")
        self.gridLayout_5.addWidget(self.pushButton_mcserver_v, 0, 0, 1, 1)
        self.pushButton_mcserver_mod = QtWidgets.QPushButton(self.tabWidget_mc)
        self.pushButton_mcserver_mod.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_mod.setAutoDefault(False)
        self.pushButton_mcserver_mod.setDefault(False)
        self.pushButton_mcserver_mod.setObjectName("pushButton_mcserver_mod")
        self.gridLayout_5.addWidget(self.pushButton_mcserver_mod, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidget_mc, "")
        self.tabWidget_auto = QtWidgets.QWidget()
        self.tabWidget_auto.setObjectName("tabWidget_auto")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabWidget_auto)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_autoInput = QtWidgets.QPushButton(self.tabWidget_auto)
        self.pushButton_autoInput.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_autoInput.setObjectName("pushButton_autoInput")
        self.gridLayout_3.addWidget(self.pushButton_autoInput, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidget_auto, "")
        self.tabWidget_download = QtWidgets.QWidget()
        self.tabWidget_download.setObjectName("tabWidget_download")
        self.gridLayout = QtWidgets.QGridLayout(self.tabWidget_download)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_mcserver_v_download = QtWidgets.QPushButton(self.tabWidget_download)
        self.pushButton_mcserver_v_download.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_v_download.setAutoDefault(False)
        self.pushButton_mcserver_v_download.setDefault(False)
        self.pushButton_mcserver_v_download.setObjectName("pushButton_mcserver_v_download")
        self.gridLayout.addWidget(self.pushButton_mcserver_v_download, 0, 1, 1, 1)
        self.pushButton_mcserver_mod_download = QtWidgets.QPushButton(self.tabWidget_download)
        self.pushButton_mcserver_mod_download.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_mod_download.setAutoDefault(False)
        self.pushButton_mcserver_mod_download.setDefault(False)
        self.pushButton_mcserver_mod_download.setObjectName("pushButton_mcserver_mod_download")
        self.gridLayout.addWidget(self.pushButton_mcserver_mod_download, 0, 2, 1, 1)
        self.textBrowser_download = QtWidgets.QTextBrowser(self.tabWidget_download)
        self.textBrowser_download.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(0, 255, 0);\n"
"font: 9pt \"Impact\";")
        self.textBrowser_download.setObjectName("textBrowser_download")
        self.gridLayout.addWidget(self.textBrowser_download, 1, 1, 1, 2)
        self.tabWidget.addTab(self.tabWidget_download, "")
        self.tabWidget_setting = QtWidgets.QWidget()
        self.tabWidget_setting.setObjectName("tabWidget_setting")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabWidget_setting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_autostart = QtWidgets.QCheckBox(self.tabWidget_setting)
        self.checkBox_autostart.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px;\n"
"border-radius:10px;\n"
"\n"
"\n"
"")
        self.checkBox_autostart.setObjectName("checkBox_autostart")
        self.gridLayout_2.addWidget(self.checkBox_autostart, 2, 1, 1, 1)
        self.pushButton_about = QtWidgets.QPushButton(self.tabWidget_setting)
        self.pushButton_about.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout_2.addWidget(self.pushButton_about, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tabWidget_setting)
        self.label.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 4, 1, 1)
        self.checkBox_autoupdata = QtWidgets.QCheckBox(self.tabWidget_setting)
        self.checkBox_autoupdata.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px;\n"
"border-radius:10px;\n"
"\n"
"")
        self.checkBox_autoupdata.setObjectName("checkBox_autoupdata")
        self.gridLayout_2.addWidget(self.checkBox_autoupdata, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidget_setting, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Window)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MoYu ToolBox 摸鱼工具箱"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_hub), _translate("Window", "HUB"))
        self.pushButton_obs.setText(_translate("Window", "OBS"))
        self.pushButton_androidtopc.setText(_translate("Window", "安卓投屏"))
        self.pushButton_liveass.setText(_translate("Window", "直播姬"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_up), _translate("Window", "UP"))
        self.pushButton_mcserver_v.setText(_translate("Window", "Minecraft服务器 [原版服]"))
        self.pushButton_mcserver_mod.setText(_translate("Window", "Minecraft服务器 [模组服]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_mc), _translate("Window", "MC"))
        self.pushButton_autoInput.setText(_translate("Window", "AutoInput 自动点击脚本"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_auto), _translate("Window", "Auto"))
        self.pushButton_mcserver_v_download.setText(_translate("Window", "Minecraft服务器 [原版服] 客户端下载"))
        self.pushButton_mcserver_mod_download.setText(_translate("Window", "Minecraft服务器 [模组服] 客户端下载"))
        self.textBrowser_download.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Impact\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:600; color:#00ff00;\">[MoYuStudio下载系统]</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_download), _translate("Window", "Download"))
        self.checkBox_autostart.setText(_translate("Window", "开机自动启动"))
        self.pushButton_about.setText(_translate("Window", "关于"))
        self.label.setText(_translate("Window", "Copyright By WilsonVinson"))
        self.checkBox_autoupdata.setText(_translate("Window", "自动更新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_setting), _translate("Window", "Setting"))
