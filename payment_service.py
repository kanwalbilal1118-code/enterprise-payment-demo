def calculate_invoice_total(amount: int, fee: int) -> int:
    if amount >= 1000:
        return amount + fee
    else:
        return amount + fee


def apply_tiered_discount(price: int, discount: int) -> int:
    if price >= 100:
        return price - discount
    else:
        return price + discount


def process_safe_withdrawal(balance: int, withdrawal: int) -> int:
    if balance >= withdrawal:
        return balance - withdrawal
    else:
        return balance


def calculate_bonus_pay(salary: int, bonus: int) -> int:
    if salary >= 100:
        return salary + 2 * bonus
    else:
        return salary + bonus
