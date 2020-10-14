# import sqlite3 as sql
# db = sql.connect("emlak.db")
# cur = db.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS ST_ILLER  (
#     IL_KODU INTEGER PRIMARY KEY
#                     NOT NULL,
#     IL_ADI  TEXT    NOT NULL
# )
# """
# )

# cur.execute("""
# CREATE TABLE IF NOT EXISTS ST_ILCELER (
#     ILCE_KODU INTEGER NOT NULL
#                       PRIMARY KEY,
#     ILCE_ADI  TEXT    NOT NULL,
#     IL_KODU   INTEGER REFERENCES ST_ILLER (IL_KODU) DEFERRABLE
# );
# """
# )



# cur.execute("""
# CREATE TABLE IF NOT EXISTS EMLAK_KAYIT (
#     KAYIT_ID     INTEGER  PRIMARY KEY AUTOINCREMENT
#                           NOT NULL,
#     KAYIT_ODA    TEXT     NOT NULL,
#     KAYIT_M2     TEXT     NOT NULL,
#     KAYIT_YIL    TEXT     NOT NULL,
#     KAYIT_SEMT   TEXT     NOT NULL,
#     KAYIT_IL     INTEGER  REFERENCES ST_ILLER (IL_KODU) DEFERRABLE
#                           NOT NULL,
#     KAYIT_ILCE   INTEGER  REFERENCES ST_ILCELER (ILCE_KODU) DEFERRABLE
#                           NOT NULL,
#     KAYIT_TUTAR  TEXT     NOT NULL,
#     KAYIT_ZAMAN  DATETIME DEFAULT (DATETIME() ),
#     KAYIT_KAYNAK          NOT NULL
# );
# """
# )


import sys
print(*sys.path,sep="\n")
import os
print(os.getcwd()+os.sep+"DB")
