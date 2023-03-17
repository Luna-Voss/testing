class Osoba:
    all = []

    def __init__(self, imie, nazwisko, wiek, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wzrost = wzrost

        Osoba.all.append(self)

    def __repr__(self):
        return f'Osoba({self.imie}, {self.nazwisko}, {self.wiek}, {self.wzrost})'


osoba1 = Osoba("Anna", "Nowak", 23, 163)
print(17)
print(osoba1)

print(vars(osoba1))

print(Osoba.all)

for instance in Osoba.all:
    print(instance.imie)
# TODO: make this work.
