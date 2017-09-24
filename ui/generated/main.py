# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        main_window.setFont(font)
        main_window.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs_container = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs_container.setObjectName("tabs_container")
        self.tab_edit = QtWidgets.QWidget()
        self.tab_edit.setObjectName("tab_edit")
        self.tab_edit_container = QtWidgets.QGridLayout(self.tab_edit)
        self.tab_edit_container.setObjectName("tab_edit_container")
        self.splitter_0 = QtWidgets.QSplitter(self.tab_edit)
        self.splitter_0.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_0.setChildrenCollapsible(False)
        self.splitter_0.setObjectName("splitter_0")
        self.left_0 = QtWidgets.QWidget(self.splitter_0)
        self.left_0.setMaximumSize(QtCore.QSize(300, 16777215))
        self.left_0.setObjectName("left_0")
        self.left_0_container = QtWidgets.QVBoxLayout(self.left_0)
        self.left_0_container.setContentsMargins(0, 0, 0, 0)
        self.left_0_container.setObjectName("left_0_container")
        self.list_files = QtWidgets.QTreeView(self.left_0)
        self.list_files.setMinimumSize(QtCore.QSize(200, 0))
        self.list_files.setMaximumSize(QtCore.QSize(300, 16777215))
        self.list_files.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.list_files.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_files.setRootIsDecorated(False)
        self.list_files.setSortingEnabled(True)
        self.list_files.setObjectName("list_files")
        self.left_0_container.addWidget(self.list_files)
        self.left_0_0 = QtWidgets.QHBoxLayout()
        self.left_0_0.setObjectName("left_0_0")
        self.button_add = QtWidgets.QPushButton(self.left_0)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_add.setIcon(icon)
        self.button_add.setIconSize(QtCore.QSize(24, 24))
        self.button_add.setObjectName("button_add")
        self.left_0_0.addWidget(self.button_add)
        self.button_open = QtWidgets.QPushButton(self.left_0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_open.setIcon(icon1)
        self.button_open.setIconSize(QtCore.QSize(24, 24))
        self.button_open.setObjectName("button_open")
        self.left_0_0.addWidget(self.button_open)
        self.left_0_container.addLayout(self.left_0_0)
        self.right_0 = QtWidgets.QWidget(self.splitter_0)
        self.right_0.setObjectName("right_0")
        self.right_0_container = QtWidgets.QVBoxLayout(self.right_0)
        self.right_0_container.setContentsMargins(0, 0, 0, 0)
        self.right_0_container.setObjectName("right_0_container")
        self.right_0_0 = QtWidgets.QGridLayout()
        self.right_0_0.setObjectName("right_0_0")
        self.button_save = QtWidgets.QPushButton(self.right_0)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_save.setIcon(icon2)
        self.button_save.setIconSize(QtCore.QSize(24, 24))
        self.button_save.setObjectName("button_save")
        self.right_0_0.addWidget(self.button_save, 0, 0, 1, 1)
        self.button_encode = QtWidgets.QPushButton(self.right_0)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/img/encode.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_encode.setIcon(icon3)
        self.button_encode.setIconSize(QtCore.QSize(24, 24))
        self.button_encode.setObjectName("button_encode")
        self.right_0_0.addWidget(self.button_encode, 0, 1, 1, 1)
        self.right_0_1 = QtWidgets.QHBoxLayout()
        self.right_0_1.setObjectName("right_0_1")
        self.edit_search = QtWidgets.QLineEdit(self.right_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_search.sizePolicy().hasHeightForWidth())
        self.edit_search.setSizePolicy(sizePolicy)
        self.edit_search.setDragEnabled(True)
        self.edit_search.setObjectName("edit_search")
        self.right_0_1.addWidget(self.edit_search)
        self.button_search_clear = QtWidgets.QToolButton(self.right_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_search_clear.sizePolicy().hasHeightForWidth())
        self.button_search_clear.setSizePolicy(sizePolicy)
        self.button_search_clear.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/img/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_search_clear.setIcon(icon4)
        self.button_search_clear.setIconSize(QtCore.QSize(24, 24))
        self.button_search_clear.setObjectName("button_search_clear")
        self.right_0_1.addWidget(self.button_search_clear)
        self.checkbox_match_case = QtWidgets.QCheckBox(self.right_0)
        self.checkbox_match_case.setChecked(True)
        self.checkbox_match_case.setObjectName("checkbox_match_case")
        self.right_0_1.addWidget(self.checkbox_match_case)
        self.checkbox_words = QtWidgets.QCheckBox(self.right_0)
        self.checkbox_words.setChecked(True)
        self.checkbox_words.setObjectName("checkbox_words")
        self.right_0_1.addWidget(self.checkbox_words)
        self.checkbox_regex = QtWidgets.QCheckBox(self.right_0)
        self.checkbox_regex.setMaximumSize(QtCore.QSize(0, 16777215))
        self.checkbox_regex.setObjectName("checkbox_regex")
        self.right_0_1.addWidget(self.checkbox_regex)
        self.button_search = QtWidgets.QPushButton(self.right_0)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_search.setIcon(icon5)
        self.button_search.setIconSize(QtCore.QSize(24, 24))
        self.button_search.setObjectName("button_search")
        self.right_0_1.addWidget(self.button_search)
        self.right_0_0.addLayout(self.right_0_1, 0, 2, 1, 1)
        self.button_save_as = QtWidgets.QPushButton(self.right_0)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/img/save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_save_as.setIcon(icon6)
        self.button_save_as.setIconSize(QtCore.QSize(24, 24))
        self.button_save_as.setObjectName("button_save_as")
        self.right_0_0.addWidget(self.button_save_as, 1, 0, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.right_0)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_delete.setIcon(icon7)
        self.button_delete.setIconSize(QtCore.QSize(24, 24))
        self.button_delete.setObjectName("button_delete")
        self.right_0_0.addWidget(self.button_delete, 1, 1, 1, 1)
        self.right_0_2 = QtWidgets.QHBoxLayout()
        self.right_0_2.setObjectName("right_0_2")
        self.edit_replace = QtWidgets.QLineEdit(self.right_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_replace.sizePolicy().hasHeightForWidth())
        self.edit_replace.setSizePolicy(sizePolicy)
        self.edit_replace.setObjectName("edit_replace")
        self.right_0_2.addWidget(self.edit_replace)
        self.button_replace = QtWidgets.QPushButton(self.right_0)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/img/replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_replace.setIcon(icon8)
        self.button_replace.setIconSize(QtCore.QSize(24, 24))
        self.button_replace.setObjectName("button_replace")
        self.right_0_2.addWidget(self.button_replace)
        self.button_replace_all = QtWidgets.QPushButton(self.right_0)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/img/replace_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_replace_all.setIcon(icon9)
        self.button_replace_all.setIconSize(QtCore.QSize(24, 24))
        self.button_replace_all.setObjectName("button_replace_all")
        self.right_0_2.addWidget(self.button_replace_all)
        self.right_0_0.addLayout(self.right_0_2, 1, 2, 1, 1)
        self.right_0_container.addLayout(self.right_0_0)
        self.edit_text = QtWidgets.QTextEdit(self.right_0)
        self.edit_text.setObjectName("edit_text")
        self.right_0_container.addWidget(self.edit_text)
        self.tab_edit_container.addWidget(self.splitter_0, 0, 0, 1, 1)
        self.tabs_container.addTab(self.tab_edit, "")
        self.tab_index = QtWidgets.QWidget()
        self.tab_index.setObjectName("tab_index")
        self.tab_index_container = QtWidgets.QGridLayout(self.tab_index)
        self.tab_index_container.setObjectName("tab_index_container")
        self.container_0 = QtWidgets.QVBoxLayout()
        self.container_0.setObjectName("container_0")
        self.top_0 = QtWidgets.QHBoxLayout()
        self.top_0.setObjectName("top_0")
        self.edit_index = QtWidgets.QLineEdit(self.tab_index)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_index.sizePolicy().hasHeightForWidth())
        self.edit_index.setSizePolicy(sizePolicy)
        self.edit_index.setObjectName("edit_index")
        self.top_0.addWidget(self.edit_index)
        self.checkbox_match_case_index = QtWidgets.QCheckBox(self.tab_index)
        self.checkbox_match_case_index.setChecked(True)
        self.checkbox_match_case_index.setObjectName("checkbox_match_case_index")
        self.top_0.addWidget(self.checkbox_match_case_index)
        self.button_index = QtWidgets.QPushButton(self.tab_index)
        self.button_index.setIcon(icon5)
        self.button_index.setIconSize(QtCore.QSize(24, 24))
        self.button_index.setObjectName("button_index")
        self.top_0.addWidget(self.button_index)
        self.button_refresh_index = QtWidgets.QPushButton(self.tab_index)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_refresh_index.setIcon(icon10)
        self.button_refresh_index.setIconSize(QtCore.QSize(24, 24))
        self.button_refresh_index.setObjectName("button_refresh_index")
        self.top_0.addWidget(self.button_refresh_index)
        self.container_0.addLayout(self.top_0)
        self.bottom_0 = QtWidgets.QSplitter(self.tab_index)
        self.bottom_0.setOrientation(QtCore.Qt.Horizontal)
        self.bottom_0.setChildrenCollapsible(False)
        self.bottom_0.setObjectName("bottom_0")
        self.list_results = QtWidgets.QTreeWidget(self.bottom_0)
        self.list_results.setMinimumSize(QtCore.QSize(200, 0))
        self.list_results.setMaximumSize(QtCore.QSize(300, 16777215))
        self.list_results.setRootIsDecorated(False)
        self.list_results.setObjectName("list_results")
        self.list_results.headerItem().setText(0, "1")
        self.browse_text = QtWidgets.QTextBrowser(self.bottom_0)
        self.browse_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.browse_text.setObjectName("browse_text")
        self.container_0.addWidget(self.bottom_0)
        self.tab_index_container.addLayout(self.container_0, 0, 0, 1, 1)
        self.tabs_container.addTab(self.tab_index, "")
        self.tab_decode = QtWidgets.QWidget()
        self.tab_decode.setObjectName("tab_decode")
        self.tab_decode_container = QtWidgets.QGridLayout(self.tab_decode)
        self.tab_decode_container.setObjectName("tab_decode_container")
        self.splitter_1 = QtWidgets.QSplitter(self.tab_decode)
        self.splitter_1.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_1.setChildrenCollapsible(False)
        self.splitter_1.setObjectName("splitter_1")
        self.list_encoded = QtWidgets.QTreeView(self.splitter_1)
        self.list_encoded.setMinimumSize(QtCore.QSize(200, 0))
        self.list_encoded.setMaximumSize(QtCore.QSize(300, 16777215))
        self.list_encoded.setRootIsDecorated(False)
        self.list_encoded.setSortingEnabled(True)
        self.list_encoded.setObjectName("list_encoded")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.browse_encoded = QtWidgets.QTextBrowser(self.splitter_2)
        self.browse_encoded.setObjectName("browse_encoded")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setChildrenCollapsible(False)
        self.splitter_3.setObjectName("splitter_3")
        self.code_table = QtWidgets.QTableWidget(self.splitter_3)
        self.code_table.setMinimumSize(QtCore.QSize(0, 80))
        self.code_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.code_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.code_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.code_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.code_table.setObjectName("code_table")
        self.code_table.setColumnCount(0)
        self.code_table.setRowCount(0)
        self.code_table.horizontalHeader().setVisible(False)
        self.code_table.verticalHeader().setHighlightSections(False)
        self.browse_decoded = QtWidgets.QTextBrowser(self.splitter_3)
        self.browse_decoded.setObjectName("browse_decoded")
        self.tab_decode_container.addWidget(self.splitter_1, 0, 0, 1, 1)
        self.tabs_container.addTab(self.tab_decode, "")
        self.gridLayout_2.addWidget(self.tabs_container, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_freq = QtWidgets.QAction(main_window)
        self.action_freq.setObjectName("action_freq")
        self.action_about = QtWidgets.QAction(main_window)
        self.action_about.setObjectName("action_about")
        self.action_exit = QtWidgets.QAction(main_window)
        self.action_exit.setObjectName("action_exit")
        self.menu.addAction(self.action_freq)
        self.menu_2.addAction(self.action_about)
        self.menu_3.addAction(self.action_exit)
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(main_window)
        self.tabs_container.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "面向英文文献的编辑与检索系统"))
        self.button_add.setText(_translate("main_window", "新建"))
        self.button_open.setText(_translate("main_window", "导入"))
        self.button_save.setText(_translate("main_window", " 保存  "))
        self.button_encode.setText(_translate("main_window", "编码"))
        self.checkbox_match_case.setText(_translate("main_window", "区分大小写"))
        self.checkbox_words.setText(_translate("main_window", "单词"))
        self.checkbox_regex.setText(_translate("main_window", "正则表达式"))
        self.button_search.setText(_translate("main_window", "   查找   "))
        self.button_save_as.setText(_translate("main_window", "另存为"))
        self.button_delete.setText(_translate("main_window", "删除"))
        self.button_replace.setText(_translate("main_window", "替换"))
        self.button_replace_all.setText(_translate("main_window", "替换所有"))
        self.tabs_container.setTabText(self.tabs_container.indexOf(self.tab_edit), _translate("main_window", "编辑"))
        self.checkbox_match_case_index.setText(_translate("main_window", "区分大小写"))
        self.button_index.setText(_translate("main_window", "检索"))
        self.button_refresh_index.setText(_translate("main_window", "刷新索引"))
        self.list_results.setSortingEnabled(True)
        self.tabs_container.setTabText(self.tabs_container.indexOf(self.tab_index), _translate("main_window", "检索"))
        self.tabs_container.setTabText(self.tabs_container.indexOf(self.tab_decode), _translate("main_window", "解码"))
        self.menu.setTitle(_translate("main_window", "检索"))
        self.menu_2.setTitle(_translate("main_window", "帮助"))
        self.menu_3.setTitle(_translate("main_window", "文件"))
        self.action_freq.setText(_translate("main_window", "词汇出现频率"))
        self.action_about.setText(_translate("main_window", "关于"))
        self.action_exit.setText(_translate("main_window", "退出"))

from . import res_rc
