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
        
        # VARIAVEIS
        self.lista = fecthall()

        # funcoes criada
        self.twohundred()
        self.viewtable.triggered.connect(self.mostrarTable)
        self.botaosalva.clicked.connect(self.salva)

    def salva(self):
        name = self.cliente.text()
        item = self.rifa.currentIndex()
        rifa = self.rifa.itemText(item)
        
        if name is not None:
            if item != 0:
                inserindo_valores(int(rifa), name)
                self.rifa.removeItem(item)
        self.rifa.setCurrentIndex(0)
        self.cliente.clear()
        self.tabela.inserindo(name, item)
        
        

    def mostrarTable(self):
        self.tabela.show()
    
    def twohundred(self):
        self.rifa.addItem(f'')
        for i, (un, ni) in enumerate(self.lista):
            if ni is None:
                self.rifa.addItem(f'{un}')


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

    def inserindo(self, nam:str, index:int):
        nome = QTableWidgetItem(nam)
        self.table.setItem(index, 1, nome)


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