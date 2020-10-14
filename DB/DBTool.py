import sqlite3 as sql
class DBTool:
    def __init__(self,dbAdres,tabloAdi=""):
        self.dbAdres = dbAdres
        self.tabloAdi = tabloAdi
        self.db = sql.connect(self.dbAdres)
        self.cur = self.db.cursor()

    def insert(self,**kwargs):
        try:
            listAlan = []
            listValue = []
            for key,value in kwargs.items():
                if key == "alan":
                    listAlan = value
                if key == "deger":
                    listValue = value

            sorgu = f"""INSERT INTO 
            {self.tabloAdi} ({",".join(listAlan)})
            VALUES  ({",".join(listValue)}) """

            self.cur.execute(sorgu)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return -1

    # a,b fonk(1,2)
    # *args fonk() ya da fonk(1,2,) ya da fonk(1,2,3,54,6,7)
    # **kwargs fonk(sart="ID = 1 and DENEME = 2",liste=2)
    
    def select(self,**kwargs):
        liste = []
        try:
            sorgu = f""" 
            SELECT * FROM {self.tabloAdi}
            """           
            for key,value in kwargs.items():
                if key == "sart":
                    sorgu = sorgu + f" WHERE {value} " 

            self.cur.execute(sorgu)
            liste = self.cur.fetchall()
        except Exception as hata:
            liste.append(f"Hata:{hata}")
        finally:
            return liste
    

    def update(self,sart,**kwargs):
        try:
            liste = []
            for key,value in kwargs.items():
                liste.append(key+ "="+value)
            metin = ",".join(liste)
            
            sorgu = f"""UPDATE {self.tabloAdi} 
            SET {metin} where {sart}
            """

            self.cur.execute(sorgu)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return -1


    def delete(self,sart):
        try:
           
            sorgu = f"""DELETE FROM  {self.tabloAdi} 
            where {sart}
            """

            self.cur.execute(sorgu)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return -1

    def __del__(self):
        self.cur.close()
        self.db.close()