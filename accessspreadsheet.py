import gspread
import readdata as rd
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
    names = rd.getProducts()["names"]
    urls = rd.getProducts()["urls"]
    index = 0
    for product in names:
        values = []
        try:
            sheet = gc.open('PetConnect Website Information').worksheet(product)
            values = sheet.get_all_values()
            values.pop(0)
        except:
            values = []
        filename = directory.joinpath(urls[index][1:] + "-products.txt")
        with open(filename.resolve(), 'w+') as file:
            file.write(str(values))
        index += 1

def get_everything():
    get_product_variations()
    get_products()