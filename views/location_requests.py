LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]
def create_location(location):
    """_summary_

    Args:
        location (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    """_summary_

    Args:
        id (_type_): _description_
        new_location (_type_): _description_
    """
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Update the value.
            LOCATIONS[index] = new_location
            break


def get_all_locations():
    """_summary_

    Returns:
        _type_: _description_
    """
    return LOCATIONS


def get_single_location(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location
