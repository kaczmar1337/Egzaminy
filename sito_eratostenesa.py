"""************************************************
Nazwa: Sito Eratostenesa
Opis: Program znajduje wszystkie liczby pierwsze w zadanym przedziale 2...n za pomocą algorytmu Sita Eratostenesa.
Parametry: brak
Zwracany typ i opis: brak (wynik wyświetlany w konsoli)
Autor: Oskar Kaczmarek
************************************************"""

def sito_eratostenesa(n):
    if n < 2:
        return []

    sito = [True] * (n + 1)
    sito[0] = sito[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sito[i]:
            for j in range(i * i, n + 1, i):
                sito[j] = False

    return [x for x in range(2, n + 1) if sito[x]]

def znajdz_liczby_pierwsze():
    while True:
        try:
            n = int(input("Podaj górną granicę przedziału (>= 2): "))
            if n < 2:
                print("Granica musi być liczbą całkowitą >= 2. Spróbuj ponownie.")
                continue
        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")
            continue

        liczby_pierwsze = sito_eratostenesa(n)
        print("\nLiczby pierwsze w przedziale 2...", n, ":", liczby_pierwsze)
        break

if __name__ == "__main__":
    znajdz_liczby_pierwsze()