def deposit_value(starting_amount, percentage, period):
    value_deposit = starting_amount * (1 + percentage / 100) ** period

    return value_deposit
