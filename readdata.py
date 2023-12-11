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
    sale = []
    cost = []
    feature= []
    for value in values:
        try:
            data = [values[0], value[1], value[3], value[2], value[4]]
            names.append(value[0])
            long_descriptions.append(value[1])
            descriptions.append(value[3])
            pictures.append(value[2])
            urls.append(value[4])
            cost.append(value[5])
            sale.append(value[6])
            feature.append(value[7])
        except:
            continue
    return {"cost":cost, "sale":sale, "feature":feature, "names": names, "descriptions":descriptions, "pictures":pictures, "urls":urls, "long-desc": long_descriptions}
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
        "product-urls":[],
        "sale":[],
        "feature":[]
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
def get_all_products():
    data = getProducts()
    url = ""
    output = {
        "product-names":[],
        "product-descriptions":[],
        "product-pictures":[],
        "product-urls":[],
        "sale":[],
        "feature":[],
        "cost":[]
    }
    for url in data["urls"]:
        filename = directory.joinpath(url[1:] + '-products.txt')
        products = []
        with open(filename.resolve(), "r") as file:
            products = eval(file.read().split("\n")[0])
        for product in products:
            output["product-names"].append(product[0])
            output["product-descriptions"].append(product[1])
            output["product-pictures"].append(product[2])
            output["product-urls"].append(product[3])
            output["sale"].append(product[5])
            output["feature"].append(product[6])
            output["cost"].append(product[4])
        
    return output


def getBlogNames(): 
    filename = directory.joinpath("blogNames.txt")
    listOfTitles = []
    with open(filename.resolve(), "r") as file: 
        listOfTitles = file.read().split("\n")
    
    return listOfTitles

# def readBlogInfo(name):
#     return 

def readBlogForIndexerPage(): 
    a = getBlogNames()
    b = [] 
    # B is a list of pointers to files. 
    # @RUTHVIKVENKATESAN IS MORE TALENTED THAN @VIHASVEGGALAM
    for x in a: 
        
        existingPath = r"/" + x
        with open(existingPath + "/content.txt") as f:
            b.append(f)

    return b 

