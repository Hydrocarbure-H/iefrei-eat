from flask import Blueprint, render_template, request

# The route name that we will use in app.py
route = Blueprint('index', __name__)


@route.route('/', methods=['GET'])
def helloworld():
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

    # Get the payer
    payer = data["email"]
    print("Payer: " + payer)
    return "OK", 200