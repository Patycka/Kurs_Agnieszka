while True:
    login = input("Czesc,Podaj login: ")
    if len(login) > 3 and login.isalpha():
           print(f'Czesc {login}')
           break

hashtag_str = "#Python#is#simple#language"
nazwa_bez_hash = hashtag_str.replace("#", "")
print(nazwa_bez_hash)
hashtag_str = "#Python#is#simple#language"


nazwa_bez_hasha = ''
for znak in hashtag_str:
    if znak == '#':
        continue
    nazwa_bez_hasha += znak
print(nazwa_bez_hasha)

