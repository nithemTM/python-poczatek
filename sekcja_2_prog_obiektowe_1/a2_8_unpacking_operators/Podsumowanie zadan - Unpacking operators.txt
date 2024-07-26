# Zad 1
from random import randint


def function_1(*args):
    print("-".join(args))


# Zad 2
def function_2(**kwargs):
    tab_item = []
    for key, value in kwargs.items():
        tab_item.append(f'{key}="{value}"')

    print(f'({",".join(tab_item)})')


# Zad 3
def function_3():
    tab_1 = []
    tab_2 = []
    a = randint(3, 10)

    for i in range(1, a):
        tab_1.append(randint(1, 10000))

    b = randint(3, 10)
    for i in range(1, b):
        tab_2.append(randint(1, 10000))

    tab_sum = [*tab_1, *tab_2]
    print(f"tab_1: {tab_1}")
    print(f"tab_2: {tab_2}")
    print(f"tab_sum: {tab_sum}")


# Zad 4
def function_4():
    dictionary_1 = {"First_name": "Ala",
                    "Last_name": "Kowalska",
                    "Age": 22}
    dictionary_2 = {"Occupation": "Specjalista IT",
                    "Favorite_language": "Python"}

    dictionary_sum = {**dictionary_1, **dictionary_2}

    print(f"dict_1: {dictionary_1}")
    print(f"dict_2: {dictionary_2}")
    function_2(**dictionary_sum)


if __name__ == "__main__":
    # Zad 1
    function_1("Funkcja", "która", "przyjmuje", "dowolną", "ilość", "argumentów", "pozycyjnych")
    # Zad 2
    function_2(first_name="Adam", last_name="Sidney", country="Poland", number="689-125-133")
    # Zad 3
    function_3()
    # Zad 4
    function_4()