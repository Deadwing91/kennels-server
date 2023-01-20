import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike",
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive",
        "location_id": 2
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
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return locations


def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return location.__dict__
    