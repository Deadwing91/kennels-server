CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "email": "ryan.t@gmail.com"
    }
]

def create_customer(customer):
    """_summary_

    Args:
        customer (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """_summary_

    Args:
        id (_type_): _description_
        new_customer (_type_): _description_
    """
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Update the value.
            CUSTOMERS[index] = new_customer
            break

def get_all_customers():
    """_summary_

    Returns:
        _type_: _description_
    """
    return CUSTOMERS


def get_single_customer(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer
    