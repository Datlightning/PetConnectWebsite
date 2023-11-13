from pathlib import Path
directory =  Path(__file__).parent.joinpath("data")

def getProducts():
    values = []
    with open(directory.joinpath("products.txt").resolve()) as file:
        values = eval(file.read().split("\n")[0])
    names = []
    descriptions = []
    pictures = []
    urls = []
    for value in values:
        names.append(value[0])
        descriptions.append(value[3])
        pictures.append(value[2])
        urls.append(value[4])
    return {"names": names, "descriptions":descriptions, "pictures":pictures, "urls":urls}
    