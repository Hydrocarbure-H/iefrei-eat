from flask import Flask
from flask_cors import CORS

from src.routes.index import route as route1

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}},
     origins="*",
     methods=["GET", "POST", "UPDATE", "DELETE", "PUT"],
     allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials", "Access-Control-Allow-Origin",
                    "Access-Control-Allow-Headers", "x-access-token", "Origin", "Accept", "X-Requested-With",
                    "Access-Control-Request-Method", "Access-Control-Request-Headers"])

# Register the route route1. Check on src/routes/movies.py
app.register_blueprint(route1)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
