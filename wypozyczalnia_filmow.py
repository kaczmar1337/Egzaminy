"""************************************************
Nazwa: System wirtualnej wypożyczalni filmów
Opis: Program implementuje klasę "Film" z metodami do zarządzania tytułem i liczbą wypożyczeń.
      Klasa umożliwia inicjalizację, ustawianie i pobieranie tytułu oraz liczbę wypożyczeń,
      a także inkrementowanie liczby wypożyczeń.
Parametry: brak
Zwracany typ i opis: brak (wynik wyświetlany w konsoli)
Autor: Oskar Kaczmarek
************************************************"""

class Film:
    def __init__(self):
        self._tytuł = ""
        self._liczba_wypożyczeń = 0

    def ustaw_tytuł(self, tytuł):
        if len(tytuł) > 20:
            raise ValueError("Tytuł filmu nie może mieć więcej niż 20 znaków.")
        self._tytuł = tytuł

    def pobierz_tytuł(self):
        return self._tytuł

    def pobierz_liczbę_wypożyczeń(self):
        return self._liczba_wypożyczeń

    def inkrementuj_liczbę_wypożyczeń(self):
        self._liczba_wypożyczeń += 1


def główna():
    print("=== System wirtualnej wypożyczalni filmów ===")

    film = Film()
    print("Zainicjalizowano obiekt filmu.")
    print(f"Tytuł: '{film.pobierz_tytuł()}', Liczba wypożyczeń: {film.pobierz_liczbę_wypożyczeń()}")

    nowy_tytuł = "Incepcja"
    film.ustaw_tytuł(nowy_tytuł)
    print(f"\nUstawiono nowy tytuł filmu: {film.pobierz_tytuł()}")

    print(f"Liczba wypożyczeń filmu: {film.pobierz_liczbę_wypożyczeń()}")

    print("\nInkrementowanie liczby wypożyczeń...")
    print(f"Przed: {film.pobierz_liczbę_wypożyczeń()}")
    film.inkrementuj_liczbę_wypożyczeń()
    print(f"Po: {film.pobierz_liczbę_wypożyczeń()}")


if __name__ == "__main__":
    główna()
