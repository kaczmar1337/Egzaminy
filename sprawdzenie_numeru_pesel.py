"""************************************************
Nazwa: Sprawdzanie numeru PESEL
Opis: Program sprawdza poprawność numeru PESEL wprowadzonego przez użytkownika na podstawie cyfry kontrolnej.
Parametry: brak
Zwracany typ i opis: brak (wynik wyświetlany w konsoli)
Autor: Oskar Kaczmarek
************************************************"""

def oblicz_sume_kontrolna(pesel):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10))
    return suma % 10

def sprawdz_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    suma_kontrolna = oblicz_sume_kontrolna(pesel)
    cyfra_kontrolna = int(pesel[-1])
    return (10 - suma_kontrolna) % 10 == cyfra_kontrolna

def pobierz_pesel():
    while True:
        pesel = input("Podaj numer PESEL (11 cyfr): ").strip()
        if len(pesel) == 11 and pesel.isdigit():
            return pesel
        print("Nieprawidłowy numer PESEL. Spróbuj ponownie.")

def sprawdzanie_peselu():
    pesel = pobierz_pesel()
    if sprawdz_pesel(pesel):
        print("\nNumer PESEL jest poprawny.")
    else:
        print("\nNumer PESEL jest niepoprawny.")

if __name__ == "__main__":
    sprawdzanie_peselu()
