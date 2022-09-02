print("hello")

# wiek = int(input("podaj swoj wiek: "))

# if wiek >= 18:
#     print("jestes pelnoletni")
# else:
#     print("jestes niepelnoletni")


# Typy zmiennych - float (liczby zmiennoprzecinkowe), int (liczby calkowite), str (typ napisowy), bool (prawda / falsz)

value_1 = True
value_2 = False

print(value_1, value_2)

# koniunkacja (logiczne and value 1 i value 2), jezeli koniunkcja jest prawda wypisz "PRAWDA"
if value_2 and value_1:
    print("koniunkcja jest prawdziwa")
else:
    print("koniunkcja falszywa")   

# alternatywa (or)
if value_2 or value_1:
    print("alternatywa jest prawdziwa")
else:
    print("alternatywa falszywa")   


if not value_1 == False:
    print("OK")


# Podaj liczbe i przypisz do zmiennej x. Jezeli x jest mniejszy od 10, to wypisz cyfra. W przeciwnym wypadku, przeanalizuj ponownie liczbe i sprawdze jezeli
# jest wieksza od 100 to wypisz setki, a w pozostalym przypadku dziesiatki.
x = 51
if x < 10:
    print("cyfra")
else:
    if x > 100:
        print("setki")
    else:
        print("dziesiatki")                


# Jezeli wiek jest rowny 18 to wypisz osiemnastolatek, jezeli wiekszy od 18 to pelnoletni, jezeli mniejszy niepelnoletni
wiek = 87
if wiek == 18:
    print("osiemnastolatek")
elif wiek > 18:
    print("pelnoletni")
else:
    print("jestes niepelnoletni")


# Zadanie 1.
# Napisz program, który wczytuje z klawiatury poprawny numer miesiąca, tzn. liczbę z przedziału
# < 1, 12 > . Sprawdz czy miesiac podany przez uzytkownika miesci się w zakresie, jezeli tak to wypisz jakis komunikat, a jezeli nie to np. niepoprawny miesiac.
