class szyfr:
    def __init__(self,slowo):
        self.napis = slowo

    def szyfruj(self,szyfr):
        # inicjalizacja tablicy z spólgłoskami
        spolgloski = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "x", "z"]
        spolgloska = ""

        # pętla sprawdzająca każdą litere danego słowa
        for x in range(len(self.napis)):
            stala_spol = x
            # pętla zapisująca ostatnia pozycję spółgłoski słowa
            for y in range(len(spolgloski)):
                if self.napis[stala_spol] == spolgloski[y]:

                    szyfr[stala_spol] = spolgloska
                    spolgloska = self.napis[x]
        # pętla sprawdzająca czy dama litera jest spółgłoską
        for z in range(len(spolgloski)):
            if self.napis[0] == spolgloski[z]:
                szyfr[0] = spolgloska
            # warunek sprawdzający czy pierwsza czy druga litera jest spółgłoską
            if self.napis[1] == spolgloski[z]:
                szyfr[1] = spolgloska

        print(szyfr)

slowo = "mandarynka"
tab = list(slowo)
tab2 = list(slowo)

d1 = szyfr(tab)
d1.szyfruj(tab2)
