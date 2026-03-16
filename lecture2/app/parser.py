import os


text_file = open('text_file.txt')

def file_parser(text_file: str)

# Receives txt and output json
# CVR
# Company Name
# Street
# Number
# Postal Code
# Town
# Email Address
    

class Company:
    def init(
        self,
        cvr: str,
        company_name: str,
        street: str,
        number: str,
        postal_code: str,
        town: str,
        email: str,
    ):

class Company:
    def __init__(
        self,
        cvr: str,
        company_name: str,
        street: str,
        number: str,
        postal_code: str,
        town: str,
        email: str,
    ):
        self.cvr = cvr
        self.company_name = company_name
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.town = town
        self.email = email

    def to_dict(self) -> dict:
        return {
            "cvr": self.cvr,
            "company_name": self.company_name,
            "street": self.street,
            "number": self.number,
            "postal_code": self.postal_code,
            "town": self.town,
            "email": self.email,
        }
