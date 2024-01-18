
import gdown
from pathlib import Path
import shutil
def get_people_pictures():
    directory = Path(__file__).parent
    source = directory.joinpath("people")
    destination = directory.joinpath("static").joinpath("images")
    expected = directory.joinpath("static").joinpath("images").joinpath('people')
    download_url = "https://drive.google.com/drive/folders/1a4VK-p-AvspYzMe1mw2Wd6gQjaHhf3z0"
    gdown.download_folder(url=download_url, quiet = True, use_cookies=True)
    try:
        shutil.rmtree(expected.resolve())
    except:
        pass
    shutil.move(source.resolve(), destination.resolve())
def update_product_pictures():
    directory = Path(__file__).parent
    source = directory.joinpath("products")
    destination = directory.joinpath("static").joinpath("images")
    expected = directory.joinpath("static").joinpath("images").joinpath('products')
    download_url = "https://drive.google.com/drive/folders/1NyULx6fbRsH7Qpj3prsu4LDtQn_9CSFN"
    gdown.download_folder(url=download_url, quiet = True, use_cookies=True)
    try:
        shutil.rmtree(expected.resolve())
    except:
        pass
    shutil.move(source.resolve(), destination.resolve())

def update_blog_pictures():
    directory = Path(__file__).parent
    source = directory.joinpath("blogimages")
    destination = directory.joinpath("static").joinpath("images")
    expected = directory.joinpath("static").joinpath("images").joinpath('blogimages')
    download_url = "https://drive.google.com/drive/folders/1-HdcouMmkO__YX7v5t6vLAxqTod2evRQ"
    gdown.download_folder(url=download_url, quiet = True, use_cookies=True)
    try:
        shutil.rmtree(expected.resolve())
    except:
        pass
    shutil.move(source.resolve(), destination.resolve())


if __name__ == "__main__":
    get_people_pictures()
    update_product_pictures()
    update_blog_pictures()