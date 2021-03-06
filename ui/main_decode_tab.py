import ast
from os import path, getcwd

from PyQt5.QtCore import QItemSelectionModel
from PyQt5.QtWidgets import QTableWidgetItem

from algorithm.huffman import huffman_decode
from ui.common import selection_flags
from ui.file_sort_filter import setup_file_view


class MainDecodeTab:
    def __init__(self, main_window):
        self.w = main_window

        self.model = None
        self.current_file = None
        self.current_row = 0
        self.setup()

    def load_file(self, file):
        with open(path.join('docs', file), 'r+', encoding='utf-8') as f:
            text = f.readlines()
            if text:
                self.w.browse_encoded.setText(text[0])
            else:
                self.w.browse_encoded.setText('')

            f.seek(0)
            d = ast.literal_eval(f.readlines()[0])
            encoding = d['encoding']
            codes = d['codes']
            encoded = d['encoded']

            sorted_codes = sorted(codes.items(), key=lambda t: len(t[1]))
            self.w.code_table.setColumnCount(len(sorted_codes))
            self.w.code_table.setRowCount(2)
            self.w.code_table.setVerticalHeaderLabels(['字符', '编码'])
            for i, t in enumerate(sorted_codes):
                self.w.code_table.setItem(0, i, QTableWidgetItem(t[0]))
                self.w.code_table.setItem(1, i, QTableWidgetItem(t[1]))
            self.w.code_table.resizeColumnsToContents()
            self.w.browse_decoded.setText(huffman_decode(encoded, codes))
        self.w.status_bar.showMessage(path.join(getcwd(), 'docs', file))

    def on_file_change(self, curr):
        if not curr:
            return
        name = self.model.data(curr.indexes()[0])
        self.load_file(name)
        self.current_file = name
        self.current_row = curr.indexes()[0].row()

    def select_current_row(self, row):
        index = self.model.docs_root().child(row, 0)
        self.w.list_encoded.selectionModel().select(index, selection_flags)
        self.w.list_encoded.scrollTo(index)

    def folder_loaded(self):
        if self.current_file is None:
            self.select_current_row(0)
        self.select_current_row(self.current_row)

    def setup(self):
        fs_model, self.model = setup_file_view(self.w.list_encoded, True)
        fs_model.directoryLoaded.connect(self.folder_loaded)
        self.w.list_encoded.selectionModel().selectionChanged.connect(self.on_file_change)
