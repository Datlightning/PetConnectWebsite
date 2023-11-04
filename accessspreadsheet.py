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
    
get_products()