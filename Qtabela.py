from pathlib import Path
from ui.ui import Ui_MainWindow as ui
from ui.main_ui import Ui_MainWindow as main
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
from sql import *
# 1) criar uma tabela com numero de rifas, nomes, e um 
# menubar(indicando quantos falta para concluir todos as rifas)

PASTA = Path(__file__).parent/"sql"
ARQUIVO = 'mysql.sql'
CAMINHO = PASTA/ARQUIVO


class Main(QMainWindow, main):
    def __init__(self):
        # metodos da classe em si
        super().__init__()
        self.setupUi(self)
        self.tabela = Tabela()
        
        # funcoes criada
        self.twohundred()
        self.viewtable.triggered.connect(self.mostrarTable)
        self.pushButton.clicked.connect(self.salva)

    def salva(self):
        self.lineEdit.clear()
        item = self.comboBox.currentIndex()
        self.comboBox.removeItem(item)
        self.comboBox.setCurrentIndex(0)
        
        

    def mostrarTable(self):
        self.tabela.show()
    
    def twohundred(self):
        self.comboBox.addItem(f'')
        for i in range(1, 201):
            self.comboBox.addItem(f'{i}')


class Tabela(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table = QTableWidget()


        self.rifas = fecthall()
        # self.coluna = colors
        # self.vertica = num_vertical
        
        self.table.setRowCount(len(self.rifas))
        self.table.setColumnCount(len(self.rifas[0]))
        self.table.setHorizontalHeaderLabels(['numero', 'pessoa'])
        self._item()

        self.box.addWidget(self.table)
        self.setLayout(self.box)

    def _item(self):
        for i, (num, code) in enumerate(self.rifas):
            item_rifa = QTableWidgetItem(f'{num}')
            if code is None:
                item_name = QTableWidgetItem("")
                self.table.setItem(i, 1, item_name)
            elif code is not None:
                item_name = QTableWidgetItem(f"{code}")
                self.table.setItem(i, 1, item_name)

            self.table.setItem(i, 0, item_rifa)