def create_expense(description, amount, category):
    return {
        "type": "expense","description": description,"amount": amount,"category": category
    }

def create_income(description, amount, category):
    return {
        "type": "income","description": description,"amount": amount,"category": category
    }