# Zad 1
class MaxLimitExpectation(Exception):
    # Zad 2
    def __init__(self, allowed_limit, message=None, *args):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"Przekroczono limit elementów zamówienia który wynosi {allowed_limit}"
        super().__init__(message, *args)
