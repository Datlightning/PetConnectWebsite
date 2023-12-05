import gdown
from pathlib import Path
import shutil

def update():
    directory = Path(__file__).parent.parent.parent
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
