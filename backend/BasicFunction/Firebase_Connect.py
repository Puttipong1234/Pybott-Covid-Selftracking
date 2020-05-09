from datetime import date
# ดึงข้อมูลจาก firebase ตาราง
def get(uid,firebase_app,database_name,all=False):
    res = firebase_app.get("/"+ database_name , None)
    if not all:
        return firebase_app.get("/"+ database_name + "/" + uid , None)
    
    else:
        return res

def get_daily_tracking(uid,firebase_app,database_name,all=False):
    today = date.today()
    res = firebase_app.get("/"+ database_name + "/"+uid+ "/" + str(today) , None)
    return res

# สร้างข้อมูล User ใหม่ขึ้นมา
def post(uid,data,firebase_app,database_name):
    # data[uid] = {"uid":"4","name":"book4","session":"greeting"}
    res = firebase_app.patch("/"+database_name+"/"+uid,data)
    return res

# สร้างข้อมูล User ใหม่ขึ้นมา
def post_daily_tracking(uid,data,firebase_app,database_name):
    # data[uid] = {"uid":"4","name":"book4","session":"greeting"}
    today = date.today()
    res = firebase_app.patch("/"+database_name+"/"+uid+"/"+str(today),data)
    return res

# อัพเดตข้อมูล User
def update(uid,new_data,firebase_app,database_name):
    res = firebase_app.patch("/"+database_name+"/"+uid , new_data)
    return res

# อัพเดตข้อมูล User
def update_daily_tracking(uid,new_data,firebase_app,database_name):
    today = date.today()
    res = firebase_app.patch("/"+database_name+"/"+uid+"/"+str(today) , new_data)
    return res

# ลบข้อมูล User
def delete(uid,firebase_app,database_name):
    res = firebase_app.delete("/"+database_name ,uid)
    return res