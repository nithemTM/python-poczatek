class TaxCalculator:
    @staticmethod
    def calculate_tax(total_price, category_name):
        if category_name == "Owoce i warzywa":
            return round(total_price * 0.05, 2)
        elif category_name == "Jedzenie":
            return round(total_price * 0.08, 2)
        else:
            return round(total_price * 0.20, 2)
