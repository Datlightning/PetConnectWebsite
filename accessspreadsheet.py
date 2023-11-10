import gspread
from pathlib import Path

directory = Path(__file__).parent.joinpath("data")
credentials = Path(__file__).parent.joinpath('creds.json')
gc = gspread.service_account(filename=credentials.resolve())

def get_products():
    sheet = gc.open('PetConnect Website Information').worksheet('Products')
    values = sheet.get_all_values()
    values.pop(0)
    filename = directory.joinpath("products.txt")
    with open(filename.resolve(), "w+") as file:
        file.write(str(values))

def get_product_variations():
    products = ["Pet Feeder", "Pet Shoes", "Pet Umbrella"]
    for product in products:
        sheet = gc.open('PetConnect Website Information').worksheet(product)
        values = sheet.get_all_values()
        values.pop(0)
        filename = directory.joinpath(product + "-products.txt")
        with open(filename.resolve(), 'w+') as file:
            file.write(str(values))

def get_everything():
    get_product_variations()
    get_products()
get_everything()