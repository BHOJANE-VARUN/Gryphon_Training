# import csv
# with open("./files/people.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name","Age"])
#     writer.writerow(["varun","20"])
#     writer.writerow(["alex","21"])

# with open("./files/people.csv","r",newline="") as file:
#     temp = csv.DictReader(file.readlines())
#     print(list(x["name"] for x in list(temp)))

# import json

# dictionary = {
#     "name": "varun",
#     "rollno": 21,
# }

# json_object = json.dumps(dictionary, indent=4)


# with open("./files/peoples.json", "w") as outfile:
#     outfile.write(json_object)

import random 
from Questions import sqaureFunc,sqaureRootFunc
from Exceptions_for_ques import InvalidChoice
from fileOperations import saveResult

def is_convertible_to_int(val):
    try:
        int(val)
        return True
    except (ValueError, TypeError):
        return False


score = 0
name = input("please Enter your name:")
results = {name:[]}
print(results)
while(True):

    try:
        choice  = input("ready for hard question(1 for yes): ")
        if is_convertible_to_int(choice)==False:
            raise InvalidChoice(choice)

        choice = int(choice)
        if(choice==1):
            funcChoice = random.randint(0,1)
            if(funcChoice==1):
                score,res = sqaureFunc(score)
                results[name].append(res)
            else: 
                score,res = sqaureRootFunc(score)
                results[name].append(res)
            if(score>=15):
                saveResult(results)
                print(f"you have reached maximum score i.e {score}")
                print("Thanks for playing")
        else:
            saveResult(results)
            print(f"final score {score}")
            print("Thanks for playing")
            break
    except InvalidChoice as e:
        print(e)




