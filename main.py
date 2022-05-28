import csv


class Polaczenia:
  def __init__(self, nazwa_pliku):
    self.nazwa_pliku = nazwa_pliku
    self.dane_słownik = self.dane()

  def dane(self):
    kom_sl = dict()
    with open(self.nazwa_pliku, 'r') as fin:
      reader = csv.reader(fin, delimiter = ",")
      naglowki = next(reader)

      for row in reader:
        dzwoniacy = int(row[0])
        if dzwoniacy not in kom_sl:
          kom_sl[dzwoniacy] = 0
        kom_sl[dzwoniacy] += 1
    return kom_sl

  def pobierz_najczesciej_dzwoniacego(self):
    return max(self.dane_słownik.items(), key= lambda x: x[1])

if __name__ == "__main__":
    print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())