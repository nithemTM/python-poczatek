class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price, "none"


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percent_discount):
        self.percent_discount = percent_discount

    def apply_discount(self, total_price):
        return total_price*self.percent_discount, "loyal"


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, decrease_value):
        self.decrease_value = decrease_value

    def apply_discount(self, total_price):
        if total_price > 500:
            return total_price-self.decrease_value, "holiday"
        else:
            return total_price, "none"

# def default_policy(total_price):
#     return total_price, "none"
#
#
# def discount_all_item(total_price):
#
#     return total_price * 0.95, "loyal"
#
#
# def discount_holiday(total_price):
#
#     if total_price > 500:
#         return total_price - 20, "holiday"
#     else:
#         return total_price, "none"


