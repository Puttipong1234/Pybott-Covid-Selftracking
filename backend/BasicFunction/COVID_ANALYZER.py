from datetime import date
from datetime import datetime

def analyze_covid_from_user(username,dict_report):
    
    today = date.today()
    now = datetime.now().strftime("%H:%M:%S")
    
    _input_current_date = str(today) + str(now) # วันที่ + เวลา ณ ตอนนั้น

    score = 0

    score += int(dict_report["มีไข้"])*4
    score += int(dict_report["มีอาการไอ"])*4
    score += int(dict_report["น้ำมูกไหล"])*4
    score += int(dict_report["มีอาการเจ็บคอ"])*4
    score += int(dict_report["เหนื่อยหอบ"])*4
    
    dict_report["score"] = score
    dict_report["วันที่"] = str(today)

    if 60 <= score < 100:
        dict_report["ข้อเสนอแนะ"] = "ควรกักตัวอยู่ที่บ้านนะคะ"

    elif score == 100:
        dict_report["ข้อเสนอแนะ"] = "ควรไปพบแพทย์เดี๋ยวนี้เลยคะ"

    else :
        dict_report["ข้อเสนอแนะ"] = "ไม่มีอาการสุ่มเสี่ยงต่อเชื่อไวรัส"
    
    return dict_report