import sqlite3 as sql
####################### İL EKLEME ################################
# db = sql.connect(r"DB\emlak.db")
# cur = db.cursor()
# dosyail = open(r"DB\2014-il-listesi__.csv","r+",encoding="UTF-8")
# dosyail.readline()

# liste = dosyail.readlines()
# for item in liste:
#     cur.execute(f""" INSERT INTO ST_ILLER (
#                          IL_KODU,
#                          IL_ADI
#                      )
#                      VALUES (
#                          {item.split(",")[0]},
#                          {item.split(",")[1].replace('"',"'")}
#                      )""")
#     db.commit()
#####################################################################

db = sql.connect(r"DB\emlak.db")
cur = db.cursor()
dosyail = open(r"DB\2014-ilce-listesi__.csv","r+",encoding="UTF-8")

liste = dosyail.readlines()
print(*liste)
for item in liste:
    print(item.split(",")[1].replace('"',"'"),item.split(",")[0])
    cur.execute(f""" INSERT INTO ST_ILCELER (  ILCE_ADI,
                           IL_KODU
                       )
                       VALUES (
                         {item.split(",")[1].replace('"',"'")},
                         {item.split(",")[0]}
                     )""")
    db.commit()