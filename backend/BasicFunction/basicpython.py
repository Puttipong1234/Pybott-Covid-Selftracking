# integer 1 ,2 3 4 5 6
x = 1
y = 2
# x + y = 3
# print(x+y) #แสดงค่า 3 ออกมา
# print(type(x+y)) #<class 'int'>

# double , float 1.00 , 1.50
x = 1.5
y = 1
# print(x+y)
# print(type(x+y)) #<class 'float'>

# String
x = "pybott1"
y = "pybott2"

# print("This is string")
# print(x+y)

# This is List
# x1 = 1
# x2 = 2
# x3 = 3
# x4 = 4

#index 0 1 2 3
    # -4-3-2-1
x =   [1,2,3,4]
result = x[1] + x[3] # 6
# print(result)

x = ["pybottครั้งที่1","pybottครั้งที่2","pybottครั้งที่3","pybottครั้งที่4"]
y = ["web programming","chatbot","network","data science"]
# การเรียนรู้ pybottครั้งที่1 เรียนเรื่อง web programming
# result = "การเรียนรู้ " + x[0] + " เรียนเรื่อง " + y[0]
# print(result)

# loop
# for valueX,valueY in zip(x,y):
#     result = "การเรียนรู้ " + valueX + " เรียนเรื่อง " + valueY
#     print(result)

# for index , value in enumerate(x):
#     print(index)
#     print(value)

# print(len(x)) #check members of list

# add สมาชิกใหม่ หรือ ลบ สมาชิค ออกจากลิส

x = ["pybottครั้งที่1","pybottครั้งที่2","pybottครั้งที่3","pybottครั้งที่4"]
y = ["web programming","chatbot","network","data science"]

number = [1,2,3,4,5,6,7,8,9]
# print(number[2:7])

# print(x)

# x.append("pybottครั้งที่5")
# print(x)

# x.pop(0)
# print(x)

# x.remove("pybottครั้งที่5")
# print(x)

# set , tuple
# tuple1 = (1,2,3,4)
# print(tuple1[0])
# tuple1[0] = 0
# print(tuple1[0])


# number = [1,2,3,4,5,6,7,8,9]
# list comprehension
# index ที่ 0 มีค่าเท่ากับ 1
# print([str(index) + "มีค่าเท่ากับ" + str(value) for index,value in enumerate(number)])


# set
# emaple_set = {1,2,3,4,5}

# dictionary key-value
            #    key    value    key    value
# exmaple_dict = {"cat" : "แมว" , "dog" : "สุนัข"}

# result = exmaple_dict["dog"] #สุนัข

# loop , add , remove

# example_user_1 = {
#     "name" : "Uncle Engineer",
#     "country" : "thailand",
#     "address" : "bangkok",
#     "Infected_Corona_virus": False
# }

# example_user_2 = {
#     "name" : "Uncle Pybott",
#     "country" : "laos",
#     "address" : "aaaaaa",
#     "Infected_Corona_virus": True
# }

# print("สถานะการติดเชื้อของคุณ  " + example_user_2["name"] + "  มีผลลัพธ์ดังนี้  " + str(example_user_2["Infected_Corona_virus"]))

# from datetime import date

# print("ยินดีต้องรับเข้าสู่บริการตรวจคัดกรองไวรัส COVID-19 \n คุณควรจะกักตัวหรือไม่")
# _input_name = input("กรุณากรอกชื่อของท่าน :   ")
# print("สวัสดีคุณ : " + _input_name)
# _input_has_fever = input("คุณ" + _input_name+" มีไข้สูงมากกว่า 37.5 องศา หรือไม่? (y/n) :   ")
# _input_has_cought = input("คุณ" + _input_name+" มีอาการไอหรือไม่ (y/n) :   ")
# _input_has_เจ็บคอ = input("คุณ" + _input_name+" มีอาการเจ็บคอหรือไม่ (y/n) :   ")
# _input_has_น้ำมูกไหล = input("คุณ" + _input_name+" มีอาการน้ำมูกไหลหรือไม่ (y/n) :   ")
# _input_has_เหนื่อยหอบ = input("คุณ" + _input_name+" มีอาการายใจเหนื่อยหอบ หายใจลำบากไหลหรือไม่ (y/n) :   ")
# today = date.today()
# _input_current_date = today

# print("สรุปจากผลการตรวจสอบอาการเบื้องต้น พบว่า")
# score = 0

# if _input_has_fever == "y":
#     score += 20
    
# if _input_has_cought == "y":
#     score += 20
    
# if _input_has_น้ำมูกไหล == "y":
#     score += 20

# if _input_has_เจ็บคอ == "y":
#     score += 20

# if _input_has_เหนื่อยหอบ == "y":
#     score += 20

# print("คุณ" + _input_name)
# if score >= 60:
#     print("ควรกักตัวอยู่ที่บ้านนะคะ")

# elif score == 100:
#     print("ควรไปพบแพทย์เดี๋ยวนี้เลยคะ")

# else :
#     print("ไม่มีอาการสุ่มเสี่ยงต่อเชื่อไวรัส COVID-19")

# print("ข้อมูลการตรวจเฝ้าระวังวันที่ " + str(today))


# สรุป Database Model , DB relationship
# 1 user มีการกรอกได้หลายวัน
# 1 วัน มีข้อมูล _input_has_fever , _input_has_cought ,_input_has_เจ็บคอ
#           _input_has_น้ำมูกไหล , _input_has_เหนื่อยหอบ , วันที่ , score

dict_วันที่1 = {
    "มีไข้" : True,
    "มีอาการไอ" : True,
    "มีอาการเจ็บคอ" : True,
    "น้ำมูกไหล" : True,
    "เหนื่อยหอบ" : True,
    "วันที่" : "2020-04-04",
    "score" : 100
}

dict_วันที่2 = {
    "มีไข้" : True,
    "มีอาการไอ" : True,
    "มีอาการเจ็บคอ" : True,
    "น้ำมูกไหล" : True,
    "เหนื่อยหอบ" : False,
    "วันที่" : "2020-04-05",
    "score" : 80
}

database = {
    
    "username1" : [dict_วันที่1,dict_วันที่2] ,
    
    "username2" : [dict_วันที่1,dict_วันที่2]
    
}

import pprint
pprint.pprint(database,indent=2)

# google Firebase