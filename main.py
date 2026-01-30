import sys
from PySide6.QtWidgets import QApplication
from Qtabela import Tabela

if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Tabela(2, 200)
    table.show()
    app.exec()