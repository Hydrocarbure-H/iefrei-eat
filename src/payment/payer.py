class Payer:
    def __init__(self, email):
        self.email = email

    def check_email(self):
        if not self.email.endswith("@efrei.net"):
            raise Exception("Invalid email address")

    def __str__(self):
        return self.email
