from flask import Blueprint, render_template, request

from src.payment.payer import Payer

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
    # Render index.html page

    return render_template("success.html")


@route.route('/order', methods=["POST"])
def create_order():
    """
    Create an order
    :return:
    """
    # Get data
    data = request.get_json()

    # Create payer
    try:
        payer = Payer(data["email"])
    except Exception as e:
        return str(e), 400

    # Create order
    payer.set_order(data["order"])

    # Write to database
    try:
        payer.write_to_db()
    except Exception as e:
        print(e)
        return str(e), 400

    return "OK", 200