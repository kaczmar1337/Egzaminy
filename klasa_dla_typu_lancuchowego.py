"""************************************************
Nazwa: Klasa dla typu łańcuchowego
Opis: Program implementuje klasę z metodami narzędziowymi dla łańcuchów znaków.
      Klasa zawiera dwie metody:
      - Liczenie samogłosek w łańcuchu znaków.
      - Usuwanie powtórzeń znaków występujących obok siebie.
Parametry: brak
Zwracany typ i opis: brak (wynik wyświetlany w konsoli)
Autor: Oskar Kaczmarek
************************************************"""

class NarzędziaTekstowe:
    @staticmethod
    def policz_samogłoski(tekst):
        if not tekst:
            return 0
        samogłoski = "aąeęiouóyAĄEĘIOUÓY"
        return sum(1 for znak in tekst if znak in samogłoski)

    @staticmethod
    def usuń_powtórzenia_znaków(tekst):
        if not tekst:
            return ""
        wynik = [tekst[0]]
        for znak in tekst[1:]:
            if znak != wynik[-1]:
                wynik.append(znak)
        return ''.join(wynik)


def główna():
    print("=== Narzędzia dla łańcuchów znaków ===")
    tekst_użytkownika = input("Podaj łańcuch znaków: ").strip()

    liczba_samogłosek = NarzędziaTekstowe.policz_samogłoski(tekst_użytkownika)
    print(f"Liczba samogłosek w podanym łańcuchu: {liczba_samogłosek}")

    oczyszczony_tekst = NarzędziaTekstowe.usuń_powtórzenia_znaków(tekst_użytkownika)
    print(f"Łańcuch po usunięciu powtórzeń: {oczyszczony_tekst}")


if __name__ == "__main__":
    główna()
