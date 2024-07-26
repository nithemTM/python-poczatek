import random


# Zad 1
def clear_white_sign(f_name,l_name):
    return f_name.strip(), l_name.strip()


first_name = input("Podaj swoje imie: ")
last_name = input("Podaj swoje nazwisko: ")

first_name, last_name = clear_white_sign(first_name,last_name)

print(f"Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)")


# Zad 2
def random_id(i):
    for x in range(0,i):
        id_random = random.randint(0,100)
        print(f"Losowy identyfikator nr {x}: {str(id_random).zfill(5)}")


index = int(input("Podaj ile potrzebujesz losowych identyfikatorów: "))
random_id(index)


# Zad 3
def checking(color_ex):
    if str(color_ex).find("niebieski",-1):
        print("Znajduje się wśród Twoich ulubionych kolorów -> niebieski")
    else:
        print("Brak koloru -> niebieskiego")


color = input("Podaj swoje ulubione kolory(rozdziel je przecinkiem): ")
checking(color)


# Zad 4
print("Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)".format(first_name=first_name, last_name=last_name))
print("Nazywasz się %(first_name)s %(last_name)s - jak miło Cię poznać :)" % {"first_name": first_name, "last_name": last_name})
