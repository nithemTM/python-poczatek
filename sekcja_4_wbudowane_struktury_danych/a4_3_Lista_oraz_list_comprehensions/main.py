
# Zad 1
print("Liczby podzielne przez 3:")
list_3 = [number for number in range(1, 31) if number % 3 == 0]
print(list_3)
list_5 = [number for number in range(1, 31) if number % 5 == 0]
print("Liczby podzielne przez 5:")
print(list_5)
print("Połączone listy:")
list_3 += list_5
print(list_3)

# Zad 2
print("Lista ulubionych sportów!")

favorite_s = []
while True:
    f_sport = input("Podaj ulubiony sport lub zakończ (Z): ")
    if f_sport == "Z":
        break
    favorite_s.append(f_sport)

if len(favorite_s) < 2:
    print("Za mało ulubionych psortów żeby wyświetlić co drugi!")
else:
    print(favorite_s[1::2])

