from pathlib import Path
from ui.ui import Ui_MainWindow
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
import sqlite3
# 1) criar uma tabela com numero de rifas, nomes, e um 
# menubar(indicando quantos falta para concluir todos as rifas)

PASTA = Path(__file__).parent/"sql"
ARQUIVO = 'mysql.sql'
CAMINHO = PASTA/ARQUIVO


class Tabela(QMainWindow,Ui_MainWindow):
    def __init__(self, num_colunm:int, num_vertical:int):
        super().__init__()

        self.table = QTableWidget()
        
        self.setupUi(self)

        self.coluna = num_colunm
        self.vertica = num_vertical
        
        self.table.setColumnCount(self.coluna)
        self.table.setRowCount(self.vertica)
        self.table.setHorizontalHeaderLabels(['numero', 'pessoa'])

        self.item_()


        self.box.addWidget(self.table)


    def item_(self):
        for num in range(0,self.vertica+1):
            self.item_rifa = QTableWidgetItem(num)
            self.table.setItem(num,0,self.item_rifa)

    


