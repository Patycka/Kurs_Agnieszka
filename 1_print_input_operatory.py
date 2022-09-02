print("Hello world")
print("23")
print('23')
print(23)

# Zadanie wyswietl Cześć Anna, twój wiek = 18
print("Cześć Anna, twój wiek = 18")
wiek = 27
print(type(wiek))
print(wiek)
print(f"Cześć Anna, twój wiek = {wiek}")

# imie = input("Podaj swoje imie: ")
# wiek = int(input("Podaj swoj wiek: "))
#
# print(type(wiek))
# print(f"Cześć {imie} , Twoj wiek to {wiek}")
# print(type(imie))
#
# # Sprawdzenie czy wiek jest wiekszy od 18, jezeli tak to wypisujemy tekst "Jesteś pełnoletnia"
# if wiek > 18:
#     print("Jestes pelnoletnia")

# Typy zmiennych
# string str - typ napisowy, "Hello", "1"
# liczba calkowita int - 1, 2, 5, 10, 27
# float - zmiennoprzecinkowy - 2.3, 5.6, 2.33333, -3.5

waga = 2.3
print(waga)
print(type(waga))

# Operatory = (przypisania), +, -, *, /, 2**3
saldo = 100
print(saldo)
saldo = saldo + 200
print(saldo)
saldo = saldo - 150
print(saldo)
# Operator skrocony zwiekszania
saldo += 100
print(saldo)
saldo *= 2 # saldo = saldo * 2
print(saldo)
saldo /= 100
print(saldo)
# Podnies do potegi 3
saldo **= 3
print(saldo)

# Operator reszty % (modulo)
print(10 % 3) # wynik 1
print(9 % 3) # wynik 0

import math
wynik = math.sqrt(25)
print(wynik)


'''
Praca domowa: 
1. Wyswietl swoje imie i hobby, wazne aby hobby bylo wyswietlone w nowej linii, np.
Ania
Siatkowka
(Wskazówka: w środku print można wstawić znak nowej linii: \n lub użyć 2 oddzielnych printów)

2. Za pomocą funkcji input poproś użytkownika o podanie ulubionego przedmiotu.
Następnie wyśiwetl komunikat: Twój ulubiony przedmiot to: np. chemia

3. Podaj za pomocą input() dugosc boku i nastepnie oblicz pole kwadratu o takim boku, przypisz
wynik do zmiennej i wyświetl pole
(Wskazówka: pamiętaj, że input zwraca string jeżeli chcesz wykonywać obliczenia należy zmienną
zrzutować na int, tak jak w przykładzie z wiekiem)

4. Podaj do input() ilość sekund. Następnie za pomocą obliczeń oblicz ile to godzin.
Wyświetl informację: x sekund = y godzin, gdzie x to liczba podana w input a y obliczona ilość godzin.
'''

