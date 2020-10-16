import sys
import os
sys.path.append(os.getcwd()+os.sep+"DB")
sys.path.append(os.getcwd()+os.sep+"BS4")
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from DBTool import DBTool
from emlak1 import Emlak1


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DBTool(r"DB\emlak.db")
        self.initUI()
        

    def initUI(self):
        uic.loadUi(r"UI\AnaMenu.ui",self)
        self.comboDoldur()
        self.cmbIL.currentTextChanged.connect(self.cmbIlceDoldur)
        self.btVeriCek.clicked.connect(self.VeriCek)
        self.show()

    def cevrim(self,param):
        return param.replace("ç","c").replace("ı","i").replace("ş","s").replace("ö","o").replace("ü","u")


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

    def VeriCek(self):
        veri = Emlak1()
        il = self.cmbIL.currentText().lower()
        ilce = self.cevrim(self.cmbilce.currentText().lower())
        # print(il,ilce)
        self.lblSayi.setText(str(self.hs.value()))
        for i in range(int(self.hs.value())):
            self.pB.setValue(i*5)
            print(*veri.veriCek(rf"https://www.sahibinden.com/satilik-daire/{il}-{ilce}?pagingOffset={i*10}&pagingSize=50"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())