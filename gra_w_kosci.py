"""************************************************
Nazwa: Gra w kości
Opis: Program implementuje logikę gry w kości. Użytkownik wybiera liczbę kości do rzutu,
losowane są wartości z przedziału 1-6. Program oblicza punkty za rzuty według ustalonych zasad.
Parametry: brak
Zwracany typ i opis: brak (wynik wyświetlany w konsoli)
Autor: Oskar Kaczmarek
************************************************"""

import random

def losuj_kosci(liczba_kosci):
    return [random.randint(1, 6) for _ in range(liczba_kosci)]

def oblicz_punkty(wartosci):
    punkty = 0
    for wartosc in set(wartosci):
        if wartosci.count(wartosc) > 1:
            punkty += wartosc
    return punkty

def gra_w_kosci():
    while True:
        try:
            liczba_kosci = int(input("Ile kości chcesz rzucić? (3 - 10): "))
            if 3 <= liczba_kosci <= 10:
                break
            else:
                print("Podaj liczbę z przedziału 3 - 10.")
        except ValueError:
            print("Proszę podać liczbę całkowitą.")

    wyniki = losuj_kosci(liczba_kosci)
    print("\nWyniki rzutów:")
    for i, wynik in enumerate(wyniki, start=1):
        print(f"Kość {i}: {wynik}")

    punkty = oblicz_punkty(wyniki)
    print(f"\nLiczba uzyskanych punktów: {punkty}")

    while True:
        kontynuacja = input("Jeszcze raz? (t/n): ").strip().lower()
        if kontynuacja == 't':
            gra_w_kosci()
            break
        elif kontynuacja == 'n':
            print("Dziękujemy za grę!")
            break
        else:
            print("Proszę podać 't' lub 'n'.")

if __name__ == "__main__":
    gra_w_kosci()