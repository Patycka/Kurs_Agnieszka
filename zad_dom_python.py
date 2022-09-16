slownik = {'a':100, 'b':200, 'c':300, 'd':400}
suma = 0
for i in slownik.values():
    suma += i
print(suma)

zdanie = 'Lubię matematykę i lubię programować w języku python'
zdanie = zdanie.lower()
slowa = zdanie.split()

# zbior_slow = set(slowa) # set nie rozpoznał dublikatów
# unikatowe_slowa = list(zbior_slow) 
# print(unikatowe_slowa)

zdanie_bez_dublikatow = []
for slowo in slowa:
    # Zapisywanie i ale tylko wtedy gdzie nie ma go jeszcze w liscie zdanie_bez_dublikatow
    if slowo not in zdanie_bez_dublikatow:
        zdanie_bez_dublikatow.append(slowo)
print(zdanie_bez_dublikatow)
nowe_zdanie = ' '.join(zdanie_bez_dublikatow)
print(nowe_zdanie)

# Przyklad
lista = ['1', '2', '3', '4']
nowy_string = ';'.join(lista)
print(nowy_string)


napis = 'Ala ma kota ooo'
slownik = {}

for i in napis:
    i = i.upper()
    if i != ' ':
        if i in slownik:
            slownik[i] += 1
        else:
            slownik[i] =  1

print(slownik)
max_value = max(slownik.values())
for key, value in slownik.items():
    if value == max_value:
        print(key)


#naj_litera= max(slownik, key=slownik.get)
# print(naj_litera)

    
