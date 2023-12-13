import gspread
import readdata as rd
from pathlib import Path
from random import randint
import accessfolders as af

directory = Path(__file__).parent.joinpath("data")
credentials = Path(__file__).parent.joinpath('creds.json')
gc = gspread.service_account(filename=credentials.resolve())
def get_names():
    
    sheet = gc.open('PetConnect Website Information').worksheet('People')
    values = sheet.get_all_values()
    values.pop(0)
    filename = directory.joinpath("people.txt")
    with open(filename.resolve(), "w+") as file:
        file.write(str(values))
        file.close()
    return 
def get_products():
    sheet = gc.open('PetConnect Website Information').worksheet('Products')
    values = sheet.get_all_values()
    values.pop(0)
    sale = {
        0: "",
        # 1: "Sale",
        1: "New"
    }
    featured = {
        0: "",
        1: "best-seller",
        2: "top-featured"
    }
    completed_featured = set()
    for i, line in enumerate(values):
        number = randint(0,1)
        values[i].append(sale[number])
        number = randint(0,2)
        while not number in completed_featured:
            number = randint(0,2)
            if not number in completed_featured:
                break
        completed_featured.add(number)
        if len(completed_featured) == 3:
            completed_featured = set()
        values[i].append(featured[number])
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
            sale = {
                0: "",
                # 1: "Sale",
                1: "New"
            }
            featured = {
                0: "",
                1: "best-seller",
                2: "top-featured"
            }
            completed_featured = set()
            for i, line in enumerate(values):
                number = randint(0,1)
                values[i].append(sale[number])
                number = randint(0,2)
                # # while not number in completed_featured:
                # #     number = randint(0,2)
                # #     if not number in completed_featured:
                # #         break
                # completed_featured.add(number)
                # if len(completed_featured) == 3:
                #     completed_featured = set()
                values[i].append(featured[number])
            
        except:
            values = []
        filename = directory.joinpath(urls[index][1:] + "-products.txt")
        with open(filename.resolve(), 'w+') as file:
            file.write(str(values))
        index += 1

def get_everything(pictures):
    get_products()
    get_product_variations()
    get_names()
    if pictures:
        af.update()
        af.get_people_pictures()

get_everything(False)