from flask import Blueprint, render_template, request

from src.payment.payer import Payer
from src.utils.utils import read_json

# The route name that we will use in app.py
route = Blueprint('index', __name__)


@route.route('/', methods=['GET'])
def index():
    """
    Say hello to the world
    :return:
    """
    # Render index.html page
    return render_template("index.html")


@route.route('/success', methods=['GET'])
def success():
    """
    Say hello to the world
    :return:
    """
    # Create payer
    try:
        payer = Payer(request.args.get("email"))
    except Exception as e:
        return str(e), 400

    # Get the order
    try:
        order = payer.get_order()
    except Exception as e:
        return str(e), 400

    # Render index.html page
    return render_template("success.html", order=order)


@route.route('/order', methods=["POST"])
def create_order():
    """
    Create an order
    :return:
    """
    # Get data
    data = request.get_json()

    # Create payer
    print("Creating payer...", end="", flush=True)
    try:
        payer = Payer(data["email"])
    except Exception as e:
        print("Failed", flush=True)
        return str(e), 400
    print("OK", flush=True)

    # Create order
    payer.set_order(data["order"])

    # Write to database
    print("Writing to database...", end="", flush=True)
    try:
        payer.write_to_db()
    except Exception as e:
        print("Failed", flush=True)
        print(e, flush=True)
        return str(e), 400

    print("OK", flush=True)
    return "OK", 200


@route.route('/list', methods=["GET"])
def admin_display():
    """
    Create an order
    :return:
    """
    # Get data from json
    print("Getting data from json...", end="", flush=True)
    try:
        data = read_json()
    except Exception as e:
        print("Failed", flush=True)
        return str(e), 400

    # Calculate summary : list of principals, secondarys, drinks,products
    summary = {
        "principals": [],
        "secondarys": [],
        "drinks": [],
        "products": []
    }
    for order in data["orders"]:
        print(order)
        if order["order"]["order_type"] == "with_form":
            summary["principals"].append(order["order"]["principal"])
            summary["secondarys"].append(order["order"]["secondary"])
            summary["drinks"].append(order["order"]["drink"])
        elif order["order"]["order_type"] == "no_form":
            summary["products"].append(order["order"]["no_form_product"])

    print(summary)

    return render_template("admin.html", data=data["orders"], summary=summary)
