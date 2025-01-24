"""
************************************************
klasa: Program do obsługi notatek
opis: Program konsolowy do obsługi notatek
pola: brak (program korzysta z funkcji i jednej klasy Note)
autor: Oskar Kaczmarek
************************************************
"""

class Note:
    counter = 0

    def __init__(self, title, content):
        Note.counter += 1
        self.id = Note.counter
        self.title = title
        self.content = content

    def display(self):
        print(f"Notatka #{self.id}: {self.title}\n{self.content}\n")

    def debug(self):
        print(f"DEBUG - ID: {self.id}, Title: {self.title}, Content: {self.content}")

if __name__ == "__main__":
    notes = []

    while True:
        print("\nMenu:\n1. Dodaj notatkę\n2. Wyświetl wszystkie notatki\n3. Debuguj notatki\n4. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Podaj tytuł notatki: ")
            content = input("Podaj treść notatki: ")
            note = Note(title, content)
            notes.append(note)
            print("Notatka została dodana.")
        elif choice == "2":
            if notes:
                for note in notes:
                    note.display()
            else:
                print("Brak notatek do wyświetlenia.")
        elif choice == "3":
            for note in notes:
                note.debug()
        elif choice == "4":
            print("Zamykanie programu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")