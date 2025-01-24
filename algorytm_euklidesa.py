"""
************************************************
klasa: Algorytm Euklidesa
opis: Program konsolowy do znajdowania największego wspólnego dzielnika (NWD) dwóch liczb
pola: brak (program korzysta z funkcji, nie klas z polami)
autor: Oskar Kaczmarek
************************************************
"""
def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if __name__ == "__main__":
    try:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))

        if a <= 0 or b <= 0:
            print("Liczby muszą być dodatnie!")
        else:
            wynik = nwd(a, b)
            print(f"Największy wspólny dzielnik liczb {a} i {b} to: {wynik}")
    except ValueError:
        print("Podano nieprawidłową wartość. Wprowadź liczby całkowite.")