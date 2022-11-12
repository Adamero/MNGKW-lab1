import re
import csv


def readCSVFile(nrKol: int) -> list[str]:
    wybierzKolumne = []
    with open("details.csv", "r", encoding="utf-8") as readCSVfile:
        read = csv.reader(readCSVfile)
        for line in read:
            wybierzKolumne.append(line[nrKol])

    return wybierzKolumne

def saveCSVFile(lista: list[list[str]]):
    with open('wynik.csv', 'w', newline="", encoding='utf-8') as file_write:
        f_write = csv.writer(file_write)

        for row in zip(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]):
            f_write.writerow(row)

def testWyrazeniaReg(wyrazenieReg: str, zKtorejKolumnySkorzystac: list[str]) -> list:
    wynik = []

    for wiersz in zKtorejKolumnySkorzystac:
        sprawdz = re.search(wyrazenieReg, wiersz)
        if sprawdz != None:
            wynik.append(sprawdz.group(0))
        else:
            wynik.append("")

    return wynik

def kolumna1() -> list[str]:
    return readCSVFile(0)

def kolumna2() -> list[str]:
    return readCSVFile(1)

def kolumna3() -> list[int]:
    return testWyrazeniaReg('\d*$', testWyrazeniaReg('((nr \d*)|((No|no)\W \d*)|(num\W \d*))|(iss\W \d*)', kolumna2()))

def kolumna4() -> list[int]:
    return testWyrazeniaReg('\d*$', testWyrazeniaReg('((vol.)|(Vol.)|(T\S))+ +((\d*))|( t. \d*)', kolumna2()))

def kolumna5() -> list[str]:
    return testWyrazeniaReg('e\d*', testWyrazeniaReg('(art. \w*)', kolumna2()))

def kolumna6() -> list[str]:
    return testWyrazeniaReg('((\d*)(-)(\d*))(\d)', kolumna2())

def kolumna7() -> list[str]:
    return testWyrazeniaReg('\w(\w*( |-|,|\S))*(\w*(\w*))$',testWyrazeniaReg('\w*(.)*(\w|\\\)', testWyrazeniaReg('( : )\w*(.)*(,|\\\)', kolumna1())))

def kolumna8() -> list[str]:
    return testWyrazeniaReg('^\w*', kolumna1())

def kolumna9() -> list[int]:
    return testWyrazeniaReg('(\w*)(\d\d\d\d)', kolumna1())

def main():
    saveCSVFile([kolumna1(), kolumna2(), kolumna3(), kolumna4(), kolumna5(), kolumna6(), kolumna7(), kolumna8(), kolumna9()])

if __name__ == "__main__":
    main()