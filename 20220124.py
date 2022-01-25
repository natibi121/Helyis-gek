#Készítsen osztályt, amely lakóhelyiségek alapterületét, falfelületét és a mennyezet méretét számolja ki a helyiség
#hossza, szélessége és belmagassága alapján.
#Az osztály teszteléseként kérje be, hogy hány helyiségben szeretne az illető kövezni és festeni, majd kérje be a
#helyiségek adatait. Végül addja meg, hogy mennyi kőre és falfestékre lesz szükség (az ajtók és ablakok méretét
#elhanyagoljuk).




class Helyiseg:
    def __init__(self, szelesseg, hosszusag, magassag):
        self.szelesseg = szelesseg
        self.hosszusag = hosszusag
        self.magassag = magassag

    def alapterulet(self):
        return self.szelesseg * self.magassag

    def falfelulet(self):
        return (self.hosszusag * self.magassag + self.szelesseg * self.magassag) * 2

    def festett_felulet(self):
        return self.falfelulet() + self.alapterulet()

def beolvasas():
    lista = []
    with open("helyisegek.txt","r") as file:
        for sor in file:
            adatok = sor.strip().split()
            sz = float(adatok[0])
            h = float(adatok[1])
            m = float(adatok[2])
            helyiseg = Helyiseg(sz, h, m)
            lista.append(helyiseg)
    return lista

def beker():
    helyisegek = []
    helyisegek_szama = int(input("Hány helyiségben szeretne festeni és kövezni? "))
    for i in range(helyisegek_szama):
        print(f"{i + 1}. helyiség adatai:")
        sz = float(input("\tHelyiség szélessége: "))
        m = float(input("\tHelyiség belmagassága: "))
        h = float(input("\tHelyiség hosszúsága: "))
        helyiseg = Helyiseg(sz, h, m)
        helyisegek.append(helyiseg)
    return helyisegek
    
print("Helyiségek festéséhez, kövezéséhez kalkulátor\n")
    

valasz = input("Az adott állományból olvassunk be?(i/n) ")
if valasz == "i":
    helyisegek = beolvasas()
else:
    helyisegek = beker()

print("A szükséges alapanyagok mennyisége:")
mennyiseg_m2 = 0.13
ossz_alapterulet = 0
ossz_festett_felulet = 0
for i,helyiseg in enumerate(helyisegek):
    print(f"A(z) {i+1}. helyiséghez szükséges:")
    alap_t = helyiseg.alapterulet()
    ossz_alapterulet += alap_t
    print(f"\tPadlóburkuló: {helyiseg.alapterulet()} m2")
    festett_t = helyiseg.festett_felulet()
    ossz_festett_felulet += festett_t
    print(f"\tFesték: {round(helyiseg.festett_felulet()*mennyiseg_m2)} l")

print(f"\nÖsszes szükséges padlóburkoló: {ossz_alapterulet} m2")
print(f"Összes szükséges festőanyag: {round(ossz_festett_felulet * mennyiseg_m2)} l")








    