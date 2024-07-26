from collections import namedtuple

Apple = namedtuple("Apple", ["species", "size", "price"])


def call_object():

    # Zad 1
    apple = Apple("lobo", 5, 4)

    # a
    print(apple.species)
    print(apple.size)
    print(apple.price)
    # b
    print(apple[0])
    print(apple[1])
    print(apple[2])
    # c
    for value in apple:
        print(value)


if __name__ == "__main__":
    call_object()





