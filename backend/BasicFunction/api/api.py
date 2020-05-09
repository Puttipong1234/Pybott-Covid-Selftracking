from BasicFunction.Firebase_Connect import get
from config import firebase , DB_COV_TRACKER , DB_USER_DATA , DB_USER_SESSION
from flask import jsonify
    

def get_tracking_data_by_uid(UID):
    data = get(uid=UID,firebase_app=firebase,database_name=DB_COV_TRACKER)
    user_data = get(uid=UID,firebase_app=firebase,database_name=DB_USER_DATA)
    
    
    res_data = {
        "days":len(data),
        "user_data":user_data,
        "data": data,
    }
    return jsonify(res_data)

def get_poll():
    data = firebase.get("/"+DB_COV_TRACKER,None)
    return jsonify(data)