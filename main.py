import sys
from PySide6.QtWidgets import QApplication
from Qtabela import Tabela, Main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Main()
    table.show()
    app.exec()