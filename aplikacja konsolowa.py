"""
**********************************************
nazwa programu: Aplikacja Konsolowa
opis programu: Program wczytuje dane z pliku tekstowego dotyczące albumów muzycznych, tworząc obiekty reprezentujące te dane i wyświetlając je w sformatowany sposób na konsoli.
Cel zastosowania: Zarządzanie i prezentacja danych dotyczących albumów muzycznych w przyjaznej dla użytkownika formie.
Zastosowane funkcje i klasy:
    - Klasa Album: Przechowuje dane jednego albumu, takie jak artysta, tytuł, liczba utworów, rok wydania i liczba pobrań.
    - Funkcja odczytaj_dane: Wczytuje dane z pliku tekstowego i tworzy listę obiektów klasy Album.
    - Funkcja wyswietl_dane: Wyświetla dane wszystkich albumów wczytanych z pliku w sformatowanej formie.
parametry:
    - nazwa_pliku: string - nazwa pliku tekstowego zawierającego dane albumów.
zwracany typ i opis:
    - Funkcja odczytaj_dane zwraca listę obiektów klasy Album.
    - Funkcja wyswietl_dane nie zwraca wartości, ale wyświetla dane na konsoli.
autor: Oskar Kaczmarek
**********************************************
"""

class Album:
    def __init__(self, artist, album, songsNumber, year, downloadNumber):
        self.artist = artist
        self.album = album
        self.songsNumber = songsNumber
        self.year = year
        self.downloadNumber = downloadNumber

    def __str__(self):
        return f"{self.artist}\n{self.album}\n{self.songsNumber}\n{self.year}\n{self.downloadNumber}"

def odczytaj_dane(nazwa_pliku):
    albumy = []
    try:
        with open(nazwa_pliku, encoding="utf-8") as plik:
            linie = plik.readlines()
            dane_albumu = []

            for linia in linie:
                linia = linia.strip()

                if linia:
                    dane_albumu.append(linia)
                else:
                    if len(dane_albumu) == 5:
                        try:
                            album = Album(
                                dane_albumu[0],
                                dane_albumu[1],
                                int(dane_albumu[2]),
                                int(dane_albumu[3]),
                                int(dane_albumu[4])
                            )
                            albumy.append(album)
                        except ValueError:
                            print(f"Błąd konwersji danych: {dane_albumu}")
                    else:
                        print(f"Nieprawidłowy format danych: {dane_albumu}")
                    dane_albumu = []

            if len(dane_albumu) == 5:
                try:
                    album = Album(
                        dane_albumu[0],
                        dane_albumu[1],
                        int(dane_albumu[2]),
                        int(dane_albumu[3]),
                        int(dane_albumu[4])
                    )
                    albumy.append(album)
                except ValueError:
                    print(f"Błąd konwersji danych: {dane_albumu}")

    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")
    return albumy

def wyswietl_dane(albumy):
    for album in albumy:
        print(album)
        print()

if __name__ == "__main__":
    nazwa_pliku = "Data.txt"
    albumy = odczytaj_dane(nazwa_pliku)
    wyswietl_dane(albumy)
