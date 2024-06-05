# ZADANIE 1
# from a1_2_rozne_sposoby_importowania.store.create_order import make_order
# from a1_2_rozne_sposoby_importowania.store.products import products
#
#
# print("Witamy w sklepie!")
# print("Dostepne produkty:")
# print(list(products.keys()))
#
# while True:
#     product_ord = input("Produkt: ")
#     if product_ord in products:
#         quantity_ord = int(input("Sztuki: "))
#         order = dict(make_order(product_ord, quantity_ord))
#         break
#     else:
#         print(
#             f'Nie ma takiego produktu w sklepie, poniżej dostępne:'
#             f' {list(products.keys())}')
#
# print(f"Zamówienie"
#         f'\nProdukt: {order["product"]}'
#         f'\nIlość sztuk: {order["quantity_ord"]}'
#         f'\nCałkowity koszt: {order["payment"]}'
#       )


# ZADANIE 2
# from a1_2_rozne_sposoby_importowania.store import products  -> absolutnie
# from .products import products                          -> względnie

# ZADANIE 3
from a1_2_rozne_sposoby_importowania.store.create_order import make_order
from a1_2_rozne_sposoby_importowania.store.products import products


def run():
    print("Witamy w sklepie!")
    print("Dostepne produkty:")
    print(list(products.keys()))

    while True:
        product_ord = input("Produkt: ")
        if product_ord in products:
            quantity_ord = int(input("Sztuki: "))
            order = dict(make_order(product_ord, quantity_ord))
            break
        else:
            print(
                f'Nie ma takiego produktu w sklepie! Poniżej dostępne do wyboru:'


                
                f' {list(products.keys())}')

    print(f"Zamówienie"
          f'\nProdukt: {order["product"]}'
          f'\nIlość sztuk: {order["quantity_ord"]}'
          f'\nCałkowity koszt: {order["payment"]}'
          )


if __name__ == "__main__":
    run()