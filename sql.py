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

#FECHANDO AS LIGAÇÃO
curso.close()
con.close()


def fecthall():
    connecao = sql.connect(JUNCAO)
    curs = connecao.cursor()


    curs.execute(F"SELECT rifa, name FROM {TABLE} ")
    lin = []
    lista = []
    for li in curs.fetchall():
        lin.append(li)
        lista.append(*lin.copy())
        lin.clear()


    connecao.commit()
    
    curs.close()
    connecao.close()

    return lista

# print(*fecthall())

def inserindo_valores(num:int, text:str):
    con = sql.connect(JUNCAO)
    cur = con.cursor()

    sq = f"""UPDATE {TABLE} SET 
                    name = '{text}'
                    WHERE rifa = {num} """

    cur.execute(sq)
    con.commit()

    cur.close()
    con.close()