import sqlite3 as sql
from pathlib import Path


CAMINHO = Path(__file__).parent
FILE = "sql/sqlite.sql"
JUNCAO = CAMINHO/FILE
TABLE = "rifa_pessoas"


con = sql.connect(JUNCAO)
curso = con.cursor()

# CRIANDO TABELA
curso.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} "
              "( " 
              "id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "rifa INTERGER UNIQUE, " 
              "name TEXT "
              ");")
con.commit()

#INSERINDO DADOS OU NÃO NA TBELA
sqlite = (f"INSERT OR IGNORE INTO {TABLE} " 
          "(rifa) "
          "VALUES "
          "(?) ;")
for um in range(1, 200+1): 
    curso.execute(sqlite, [um])
    con.commit()


#LISTANDO DADOS
def fecthall():
    curso.execute(F"SELECT rifa FROM {TABLE} ")

    lin = []
    for li in curso.fetchall():
        lin.append(*li)
    con.commit()
    return lin
print(*fecthall())

#FECHANDO AS LIGAÇÃO
curso.close()
con.close()
