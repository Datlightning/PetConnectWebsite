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
    long_descriptions = []
    for value in values:
        try:
            data = [values[0], value[1], value[3], value[2], value[4]]
            names.append(value[0])
            long_descriptions.append(value[1])
            descriptions.append(value[3])
            pictures.append(value[2])
            urls.append(value[4])
        except:
            continue
    return {"names": names, "descriptions":descriptions, "pictures":pictures, "urls":urls, "long-desc": long_descriptions}
def getProduct(string):
    data = getProducts()
    name = ""
    url = ""
    index = 0
    for value in data["urls"]:
        if string in value.lower():
            url = value
            name = data["names"][index]
            break
        index += 1
    output = {
        "name":name,
        "product-names":[],
        "product-descriptions":[],
        "product-pictures":[],
        "product-urls":[]
    }
    filename = directory.joinpath(url[1:] + '-products.txt')
    products = []
    with open(filename.resolve(), "r") as file:
        products = eval(file.read().split("\n")[0])
    for product in products:
        output["product-names"].append(product[0])
        output["product-descriptions"].append(product[1])
        output["product-pictures"].append(product[2])
        output["product-urls"].append(product[3])
    return output