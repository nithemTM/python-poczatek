# ZADANIE 1
# import average_speed
# distance = float(input("Podaj pokonany dystans (w km): "))
# time = float(input("Podaj czas biegu (w godz.): "))
#
# print(f"Twoja średnia prędkość to: {average_speed.average_speed(distance, time)}")

# # ZADANIE 2
# import math
#
#
# def length_side_c(side_a, side_b):
#     side_c = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
#     return side_c
#
#
# a = float(input("Podaj długość Boku A: "))
# b = float(input("Podaj długość Boku B: "))
# c = length_side_c(a, b)
# print(f"Długość przeciwprostokątnej to: {c}.")

# ZADANIE 3

starting_amount = float(input("Kwota wpłaty na lokatę (w PLN): "))
percentage = float(input("Oprocentowanie lokaty: "))
period = int(input("Na ile lat lokata: "))

ending_amount = sekcja_1_niezbednik_adepta.a1_1_pakiety_i_moduly.calculations.deposit_calculation.deposit_value(starting_amount, percentage, period)
print(f"Po {period} latach wartość Twojej lokaty wyniesie: {ending_amount}")