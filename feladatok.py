import auto


class Feladatok:
    """feladatok"""
    def __init__(self):

        pass

    def feladat_1(self, filepath: str) -> list:
        print("1. feladat: A kosar.txt beolvasása.")
        adatok = []
        try:
            inputTxt = open(filepath, "r")
            aut = inputTxt.readline().strip()
            while (aut != ""):
                adatok.append(auto.Auto(aut))
            inputTxt.close()
            return adatok
        except FileNotFoundError:
            print("File nem található!")
        pass

    def feladat_2(self,adatok:list):
        a = adatok[0].ora_leker
        b = ""
        ido = 0
        for i in range(len(adatok)):
            if a != b:
                ido += 1
            b = a
            j = i + 1
            a = adatok[j].ora_leker
        print("2. feladat: Az ellenőrzést végzők legalább ", ido, " órát dolgoztak.")

    def feladat_3(self,adatok:list):
        b = 0
        m = 0
        k = 0
        sz = 0
        for i in adatok:
            a = i.rt_leker()
            if a[0] == "B":
                b += 1
            elif a[0] == "M":
                m += 1
            elif a[0] == "K":
                k += 1
            else:
                sz += 1
        print("3. feladat: Elhaladt járművek mennyisége típusonként:")
        print("\t autóbusz: ", b, "\n\t kamion: ", k, "\n\t motor: ", m, "\n\t személygépjármű: ", sz)

    def feladat_4(self,adatok:list):
        x = ""
        y = ""
        fmi = 0
        for i in range(len(adatok)):
            if i != len(adatok):
                x1 = int(adatok[i].ora_leker) * 3600 + int(adatok[i].perc_leker) * 60 + int(adatok[i].mp_leker)
                j = i + 1
                x2 = int(adatok[j].ora_leker) * 3600 + int(adatok[j].perc_leker) * 60 + int(adatok[j].mp_leker)
                if x2 - x1 > fmi:
                    fmi = x2 - x1
                    x += adatok[i].ora_leker, ":", adatok[i].perc_leker, ":", adatok[i].mp_leker
                    y += adatok[j].ora_leker, ":", adatok[j].perc_leker, ":", adatok[j].mp_leker
        print("4. feladat: A leghosszabb forgalommentes időszak:", x, "-", y,".")
    def feladat_5(self,adatok:list):
        a=input()

    def feladat_6(self, adatok:list, filepath: str):
        print("6. feladat: Az ellenőrzések adatainak kiíratása.")
        outputTxt = open(filepath, "w")
        el="0"
        for i in range(len(adatok)):
            if adatok[i].ora_leker!=el:
                el=adatok[i].ora_leker
                outputTxt.write(adatok[i].ora_leker," Óra: ",adatok[i].rt_leker)
        outputTxt.close()
        pass