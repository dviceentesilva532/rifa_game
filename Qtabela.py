from pathlib import Path
from ui.ui import Ui_MainWindow
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
# 1) criar uma tabela com numero de rifas, nomes, e um 
# menubar(indicando quantos falta para concluir todos as rifas)

PASTA = Path(__file__).parent/"sql"
ARQUIVO = 'mysql.sql'
CAMINHO = PASTA/ARQUIVO

# colors = [("Red", "#FF0000"),
#           ("Green", "#00FF00"),
#           ("Blue", "#0000FF"),
#           ("Black", "#000000"),
#           ("White", "#FFFFFF"),
#           ("Electric Green", "#41CD52"),
#           ("Dark Blue", "#222840"),
#           ("Yellow", "#F9E56d")]





class Tabela(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        
        self.setupUi(self)

        # self.coluna = colors
        # self.vertica = num_vertical
        
        self.table.setRowCount(len(colors))
        self.table.setColumnCount(len(colors[0])+1)
        self.table.setHorizontalHeaderLabels(['numero', 'pessoa'])
        self._item()

        self.box.addWidget(self.table)
        self.setLayout(self.box)

    def _item(self):
        for i, (num, code) in enumerate(colors):
            item_rifa = QTableWidgetItem(f'{i+1}')
            item_name = QTableWidgetItem(None)
            item_code = QTableWidgetItem(code)
            self.table.setItem(i, 0, item_rifa)
            self.table.setItem(i, 1, item_name)



