# Petla for służy do powtarzania różnych operacji, a także do iteracji po elementach stringa, listy,
# zbioru, tupli i innych złożonych typów

# Napisz program wyświetlający * pięc razy, każda gwiazdka ma być w nowej linii 
print("* \n* \n* \n* \n*")

print("*")
print("*")
print("*")
print("*")
print("*")

# Wypisanie 5 gwiazdek ale za pomocą pętli for
# Funkcja range(n) zwraca sekwencję liczb, defaultowo od 0 do n-1.
# Mozna jednak przekazac argumenty range(start, stop, step)
for element in range(5):
    print("*")

# Wygeneruje liczby 3, 4, 5 z użyciem range() i for
for i in range(3, 6):
    print(i)

# Wygenerować liczby od 0 do 100. Wyświetlić tylko te, które są parzyste
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

# Wygenerować liczby od 0 do 100. Wyświetlić tylko te, które są parzyste, użyć argumentu step
for i in range(0, 101, 2):
    print(i)

# Wygenerować liczby od 0 do 100. Obliczyć sumę tych liczb i wyświetlić na koniec
suma = 0 
for i in range(0, 101):
    suma += i

print(suma)

# wyswietlić liczby od 100 do 0, trzeci argument to krok
for i in range(100, -1, -1):
    print(i)

# Iteracja po stringu, ile razy wykona się for (6)
jezyk_programowania = 'python'
for i in jezyk_programowania:
    print(i)


# Zadania
# Wygenerować liczby od -10 do 20 i wypisać tylko dodatnie oraz podzielne przez 3
for i in range(-10, 21):
    if i % 3 == 0 and i > 0:
        print(i)

# Przeiterować po stringu (twoje imie i nazwisko) i wypisać tylko literę a jeżeli wystąpi (może być a lub A)
dane = "Agnieszka Woryna"
for i in dane:
    if i == 'a' or i == 'A':
        print(i)

# Wypisać tylko pierwszy wyraz z tego stringu (output p y t h o n bez training)
string = "Python Training"
print(string[0:6])
for i in string[0:6]:
    print(i)


# Za pomocą pętli for wypisać napis ale bez hashy (#) - output lovepython
# tip: możesz spróbować stworzyć nową zmienną i doklejać do niej kolejne znaki oprócz #.
hashtag = '#love#python'
nazwa_bez_hashy = ''
for i in hashtag:
    if i != '#':
        nazwa_bez_hashy += i
print(nazwa_bez_hashy)



# Przykład pętli for wykorzystującej funkcję range()
liczby = [2, 5, 6, 7, 9, 3, 5, 8, 52]

for i in range(len(liczby)):
    print(liczby[i])


# Przykład pętli for z użyciem enumerate() 
for element in enumerate(liczby):
    print(element)