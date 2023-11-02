import json


class Payer:
    def __init__(self, email):
        self.email = email
        self.order = None
        self.check_email()

    def check_email(self):
        if not self.email.endswith("@efrei.net"):
            raise Exception("Invalid email address")

    def set_order(self, order):
        self.order = order

    def write_to_db(self):
        """
        Write the payer to the database (db.json)
        :return:
        """
        # Read the database (db.json xD)
        try:
            with open("db.json", "r") as f:
                orders = json.load(f)["orders"]
        except Exception as e:
            raise Exception("Failed to read the database: " + str(e))

        # Get the last order id
        try:
            last_order_id = orders[-1]["order"]["id"]
        except IndexError:
            last_order_id = 0
        # Create the order object
        order_o = {
            "id": last_order_id + 1,
            "email": self.email,
            "order": self.order
        }

        # Add the order to the database
        orders.append(order_o)

        # Write the database to the file
        try:
            with open("db.json", "w") as f:
                json.dump({"orders": orders}, f, indent=4)
        except Exception as e:
            raise Exception("Failed to write to the database: " + str(e))

    def __str__(self):
        return f"Payer: {self.email}, Order: {str(self.order)}"
