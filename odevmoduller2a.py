class donenVarliklar:
    kasaHesabi=20000
    alinanCeklerHesabi=10000
    bankalarHesabi=5000
    alicakSenetlerHesabi=28000
    ticariMallarHesabi=65000
class duranVarliklar:
    binalarHesabi=150000
    tasitlarHesabi=25000
    demirbaslarHesabi=8000
class kvyk:
    bankaKredileriKisa=42000
    saticilarHesabi=60000
class uvyk:
    bankaKredileriUzun=35000
    borcSenetleri=115000
class ozKaynaklar:
    sermayeHesabi=59000
class hesap():
    def __init__(self,alinanCeklerHesabi,bankalarHesabi,alicakSenetlerHesabi,ticariMallarHesabi,binalarHesabi,tasitlarHesabi,demirbaslarHesabi,bankaKredileriKısa,saticilarHesabi,bankaKredileriUzun,borçSenetleri,sermayeHesabi):
        self.kasaHesabi=kasaHesabi
        self.alinanCeklerHesabi=alinanCeklerHesabi
        self.banklarHesabi=bankalarHesabi
        self.alicakSenetlerHesabi= alicakSenetlerHesabi
        self.ticariMallarHesabi=ticariMallarHesabi
        self.binalarHesabi=binalarHesabi
        self.tasitlarHesabi=tasitlarHesabi
        self.demirbaslarHesabi=demirbaslarHesabi
        self.bankaKredileriKisa=bankaKredileriKisa
        self.saticilarHesabi=saticilarHesabi
        self.bankaKredileriUzun=bankaKredileriUzun
        self.borcSenetleri=borcSenetleri
        self.sermayeHesabi=sermayeHesabi
    def aktif(self):
        aktif=self.alinanCeklerHesabi+self.banklarHesabi+self.alicakSenetlerHesabi+self.ticariMallarHesabi+self.binalarHesabi+self.tasitlarHesabi+self.demirbaslarHesabi
        return aktif
    def pasif(self):
        pasif=self.bankaKredileriKisa+self.saticilarHesabi+self.bankaKredileriUzun+self.borcSenetleri+self.sermayeHesabi
        return pasif
    if (aktif==pasif):
        print("kapanış bilançosu doğru hesaplanmıştır")
    else:
        print("kapanış bilançosu yanlış hesaplanmıştır")
