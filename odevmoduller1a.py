class hesapla():
    def __init__(self,gelirler,giderler,toplamCiro,toplamCalisanSayisi):
        self.gelirler=gelirler
        self.giderler=giderler
        self.toplamCiro=toplamCiro
        self.toplamCalisanSayisi=toplamCalisanSayisi
    def isletmeKari(self):
        isletmeKari=self.gelirler-self.giderler
        return isletmeKari
    def adamBasiCiro(self):
        admaBasiCiro=self.toplamCiro/self.toplamCalisanSayisi
        return adamBasiCiro
