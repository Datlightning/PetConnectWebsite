from pathlib import Path
directory =  Path(__file__).parent.joinpath("data")
def get_posts():
    path = directory.joinpath('recentposts.txt')
    with open(path.resolve(), "r") as file:
        output = list(map(eval, file.read()[:-1].split("\n")))
    return output
def get_users():
    path = directory.joinpath("users.txt")
    data = []
    with open(path.resolve(), 'r') as file:
        data = list(map(eval, file.read()[:-1].split("\n")))
    return data
def create_post(username, title, picture):
    path = directory.joinpath("posts.txt")
    data = {}
    with open(path.resolve(), "r") as file:
        data  = eval(file.read())
    if username in data:
        data[username].append([title, picture])
    else:
        data[username] = [[title, picture]]
    with open(path.resolve(), "w") as file:
        file.close()
    with open(path.resolve(), "w") as file:
        file.write(str(data))
        file.close()
    path = directory.joinpath("recentposts.txt")
    with open(path.resolve(), "a") as file:
        file.write(str([username, title, picture]) + "\n")
        file.close()
def get_user_post(username):
    path = directory.joinpath("posts.txt")
    output = []
    with open(path.resolve(), "r") as file:
        data = eval(file.read())
        if username not in data:
            return []
        for information in data[username]:
            tmp = [username]
            tmp.extend(information)
            output.append(tmp)
    return output
def create_user(username, password, creator):
    path = directory.joinpath("users.txt")
    with open(path.resolve(), "a") as file:
        file.write(f"{[username, password, creator]}")
        file.write("\n")
        file.close()