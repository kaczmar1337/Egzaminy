"""************************************************
Nazwa: Sortowanie tablicy metodą bąbelkową
Opis: Program sortuje tablicę liczb całkowitych metodą bąbelkową.
Parametry: brak
Zwracany typ i opis: brak (wynik wyświetlany w konsoli)
Autor: Oskar Kaczmarek
************************************************"""
import random
def babelkowe_sortowanie(tablica):
    n = len(tablica)
    for i in range(n):
        for j in range(0, n-i-1):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    return tablica

def sortowanie_tablicy():
    tablica = [random.randint(1, 100) for _ in range(10)]
    print("Tablica przed sortowaniem:", tablica)
    posortowana = babelkowe_sortowanie(tablica)
    print("Tablica po sortowaniu:", posortowana)

if __name__ == "__main__":
    sortowanie_tablicy()