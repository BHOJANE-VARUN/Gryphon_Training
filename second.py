# l1 = [i for i in range(10)]
# l2 = [i for i in range(10,12)]
# result = list(map(lambda x,y:x+y,l1,l2))
# print(l1,l2)
# print(result)
# from functools import reduce
# students = [("ashwini",20,98,"kopargoan"),("Ram",19,97,"shirdi"),("adi",20,97,"kopargoan"),("rohit",19,88,"pune")]
#
# while(True):
#     print(" 1. collect only the name \n 2. collect the name if the marks are more then 90 \n 3.who is topper \n 4.who is youngest \n 5. how many belongs to kopargaon \n any other number to quit")
#     choice = int(input("enter a choice \n"))
#     match(choice):
#         case 1:
#             print(list(map(lambda x:x[0],students)))
#         case 2:
#             print(list(x[0] for x in (list(filter(lambda x: x[2]>=90  ,students)))))
#         case 3:
#             print(reduce(lambda x,y:x if x[2]>y[2] else y,students))
#         case 4:
#             print(reduce(lambda x, y: x if x[1] < y[1] else y, students))
#         case 5:
#             print(list(filter(lambda x:x[3]=='kopargoan',students)))
#         case _:
#             break
# collect only the name
# collect the name if the marks are more then 90
# who is topper
# who is youngest
# how many belongs to kopargaon
# name of student who are not from kopargaon
# from itertools import groupby
# data = [5,1,1,4,4,3,4,2,1,5,3,6]
# data.sort()
# groups = [list(group) for key,group in groupby(data,key=lambda x:x)]
#
# print(groups)
#
# result = [x**3 for x in range(10)]
#
# from functools import reduce
#
# '''
# objectives
# list all the employees
# who is youngest
# top performer
# top task assigned
# max task done by (name of person)
# '''
# employees = [('Aditya',19,33,20),('Deep',18,48,16),('Anisha',19,56,42),('Ganesh',20,36,24),('Pratiksha',20,45,30)]
# while True:
#   print("Menu")
#   print("1. Print all of the employees")
#   print("2. Print the youngest employee")
#   print("3. Print the top performer")
#   print("4. Print the top task assigned")
#   print("5. Print the max task done")
#   choice=int(input("Enter your choice: "))
#
#   match choice:
#     case 1:
#       li=list(map(lambda x:x[0],employees))
#       print("list of all employees: ",li)
#     case 2:
#       #youngest=min(list(map(lambda x:x[1],employees)))
#       youngest=min(employees,key=lambda x:x[1])[0]
#       print("Youngest employee: ",youngest)
#     case 3:
#       top_performer=max(employees,key=lambda x:x[2])
#       print("Top performer: ",top_performer)
#     case 4:
#       top_task_assigned=max(employees,key=lambda x:x[3])
#       print("Top task assigned: ",top_task_assigned)
#     case 5:
#       max_task_done=max(employees,key=lambda x:x[3])
#       print("Max task done: ",max_task_done)
#     case _:
#       break

# ss = {1,22,3,4,4,5}
# ss = sorted(ss)
# print(ss)

# mt = [[1,2,3],[4,5,6],[7,8,9]]
#
# trans = [list(x[i] for x in mt) for i in range(0,len(mt))]
# print(trans)
#
# result = [x*x for x in range(1,6)]
# print(result)

# dic = {x:x**3 for x in range(0,11) if x%2}
# print(dic)
# str = "engineering"
# ss = {x for x in str}
# print(ss)
# try:
#     result = int("abc")/0
#     print(result)
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)

try:
    abc = 0
    result = abc/0
    print(result)
except Exception as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print("conversion failed")
except ZeroDivisionError as e:
    print("Division by zero.")







