from pathlib import Path
directory =  Path(__file__).parent.joinpath("data")
def get_blogs():
    values = []
    filename = directory.joinpath("blogs.txt")
    with open(filename.resolve(), "r") as file:
        values = eval(file.read().split("\n")[0])
    data = {
        "names":{},
        "descriptions":{},
        "pictures":{},
        "authors":{},
        "ids":{},
        "views":{},
        "likes":{},
        "picture-descriptions":{},
        "type":{},
        "recents":[]
    }
    for d in values:
        data["names"][d[4]] = d[0]
        data["descriptions"][d[4]] = d[1].split("\n\n")
        data["pictures"][d[4]] = d[2]
        data["authors"][d[4]] = d[3]
        data["ids"][d[4]] = d[4]
        data["picture-descriptions"][d[4]] = d[5]
        data["type"][d[4]] = d[6]
        data["views"][d[4]] = d[7]
        data["likes"][d[4]] = d[8]
        data["recents"].append(d[4])

    return data
def getSignatureProducts():
    values = []
    filename = directory.joinpath("products.txt")
    with open(filename.resolve(), "r") as file:
        values = eval(file.read().split("\n")[0])
    names = []
    descriptions = []
    pictures = []
    urls = []
    long_descriptions = []
    sale = []
    cost = []
    feature= []
    ve_urls = []
    for value in values:
        try:            
            names.append(value[0])
            long_descriptions.append(value[1])
            descriptions.append(value[3])

            pictures.append(value[2])
            urls.append(value[4])
            cost.append(value[5])

            ve_urls.append(value[6])
            sale.append(value[7])
            feature.append(value[8])
            
        except:
            continue
    return {"ve-urls": ve_urls, "cost":cost, "sale":sale, "feature":feature, "names": names, "descriptions":descriptions, "pictures":pictures, "urls":urls, "long-desc": long_descriptions}
def getProduct(string):
    data = getSignatureProducts()
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
        "feature":[],
        "cost":[],
        "options":[]
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
        output["sale"].append(product[6])
        output["feature"].append(product[7])
        output["cost"].append(product[4])
        output["options"].append(product[5])
        
    return output
def add_view(blog_id):
    filename = directory.joinpath("blogs.txt")
    with open(filename.resolve(), "r") as file:
        data = eval(file.read().split("\n")[0])
    for i, line in enumerate(data):
        if blog_id == line[4]:
            data[i][7] += 1
            break
    with open(filename.resolve(), "w+") as file:
        file.write(str(data))
def get_names():
    filename = directory.joinpath("people.txt")
    output = []
    with open(filename.resolve(), "r") as file:
        output = eval(file.read().strip().split('\n')[0])
    return output
def get_all_products():
    data = getSignatureProducts()
    url = ""
    output = {
        "product-names":[],
        "product-descriptions":[],
        "product-pictures":[],
        "product-urls":[],
        "sale":[],
        "feature":[],
        "cost":[],
        "model":[],
        "type":[]
    }
    output["model"] = data["names"]
    for index, url in enumerate(data["urls"]):        
        name = data["names"][index]
        output["product-names"].append(name)
        output["product-descriptions"].append(data["descriptions"][index])
        output["product-pictures"].append(data["pictures"][index])
        output["product-urls"].append(f"/shop/{name}")
        output["sale"].append("")
        output["feature"].append('')
        output["cost"].append(data["cost"][index])
        if "bundle" in name.lower():
            output["type"].append("bundle")
        else:
            output["type"].append("individual")
        
    return output

def getProductByType(name):
    data = get_all_products()
    output = {
        "product-names":[],
        "product-descriptions":[],
        "product-pictures":[],
        "product-urls":[],
        "sale":[],
        "feature":[],
        "cost":[],
        "options":[]
    }
    for index, item in enumerate(data["type"]):
        if item == name:
            output["product-names"].append(data["product-names"][index])
            output["product-pictures"].append(data["product-pictures"][index])
            output["product-descriptions"].append(data["product-descriptions"][index])
            output["product-urls"].append(data["product-urls"][index])
            output["cost"].append(data['cost'][index])
            output["sale"].append("")
            output["feature"].append("")
    return output