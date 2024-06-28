# Zad 2
def default_policy(total_price):
    return total_price, "none"


def discount_all_item(total_price):

    return total_price * 0.95, "loyal"


def discount_holiday(total_price):

    if total_price > 500:
        return total_price - 20, "holiday"
    else:
        return total_price, "none"
