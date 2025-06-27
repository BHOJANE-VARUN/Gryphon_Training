import json

def search(name):
    with open("./database.json","r") as file:
        dic = json.load(file)
        if name in dic.keys():
            print("true")
        else:
            print("false")
search("mnou")
def saveResult(dicti):
    json_object = json.dumps(dicti, indent=4)
    with open("./database.json", "a") as outfile:
        outfile.write(json_object)
