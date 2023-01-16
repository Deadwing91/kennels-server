EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis",
        "address": "123 Fake St.",
        "locationId": 3
    }
]

def create_employee(employee):
    """_summary_

    Args:
        employee (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """_summary_

    Args:
        id (_type_): _description_
        new_employee (_type_): _description_
    """
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break

def get_all_employees():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EMPLOYEES


def get_single_employee(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee
    