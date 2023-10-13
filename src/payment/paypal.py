import time

import requests
import src.constants as CONST


class PayPal:

    def __init__(self):

        self.access_token = None

    def authenticate(self):
        """
        Authenticate with PayPal and return access token
        """

        url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials"
        }

        # Auth client_secret / client_id
        (client_id, client_secret) = CONST.CLIENT_ID, CONST.CLIENT_SECRET

        # Make request
        try:
            response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
        except Exception as e:
            raise Exception("Failure: " + str(e))

        if response.status_code != 200:
            raise Exception("Failed to authenticate with PayPal. Status code: " + str(response.status_code))

        self.access_token = response.json()["access_token"]

    def create_order(self, payer, amount):
        """
        Create an order with PayPal
        :param amount:
        :param payer:
        :return: the link to the approval url
        """

        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        data = {
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        # Reference id is the order id and a hash of the current time
                        "reference_id": str(payer.email.replace("@efrei.net", "")) + str(int(time.time())),
                        "amount": {
                            "currency_code": "EUR",
                            "value": amount
                        }
                    }
                ],
                "payment_source": {
                    "paypal": {
                        "experience_context": {
                            "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
                            "brand_name": "iEfrei Eat",
                            "locale": "fr-FR",
                            "landing_page": "LOGIN",
                            "user_action": "PAY_NOW",
                            "return_url": "https://eat.iefrei.fr?order=success",
                            "cancel_url": "https://eat.iefrei.fr?order=cancel"
                        }
                    }
                }
            }

        # Make request
        try:
            response = requests.post(url, headers=headers, json=data)
        except Exception as e:
            raise Exception("Failure: " + str(e))

        if response.status_code != 201:
            raise Exception("Failed to create order with PayPal. Status code: " + str(response.status_code))

        return response.json()["links"][1]["href"]
