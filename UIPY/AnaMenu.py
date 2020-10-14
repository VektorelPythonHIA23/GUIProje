import sys
import os
sys.path.append(os.getcwd()+os.sep+"DB")
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from DBTool import DBTool


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DBTool(r"DB\emlak.db")
        self.initUI()
        

    def initUI(self):
        uic.loadUi(r"UI\AnaMenu.ui",self)
        self.comboDoldur()
        self.btGiris.clicked.connect(self.girisYap)
        self.cmbIL.currentTextChanged.connect(self.cmbIlceDoldur)
        self.show()

  

    def comboDoldur(self):
        self.db.tabloAdi = "ST_ILLER"
        self.ilListe = self.db.select()
        self.cmbIL.setItemData(-1,"Seçiniz")
        for item in self.ilListe:
            self.cmbIL.addItem(item[1])


    def cmbIlceDoldur(self):
        self.db.tabloAdi = "ST_ILCELER"
        iladi = self.cmbIL.currentText()
        ilid = "-1"
        print(self.cmbIL.currentData())
        ilid = self.ilListe[self.cmbIL.currentIndex()][0]
        self.ilceliste = self.db.select(sart=f" IL_KODU = {ilid}")
        self.cmbilce.clear()
        for item in self.ilceliste:
            self.cmbilce.addItem(item[1])


    def girisYap(self):
        self.txtUserName.setText("Giriş yapılsın")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())