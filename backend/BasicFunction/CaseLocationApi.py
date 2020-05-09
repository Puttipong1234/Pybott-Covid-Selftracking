import requests
from fuzzywuzzy import process
import datetime
import pytz
tz = pytz.timezone('Asia/Bangkok')

def now():
    now1 = datetime.datetime.now(tz)
    month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
    thai_year = now1.year + 543
    time_str = now1.strftime('%H:%M:%S')
    # return "%d %s %d %s"%(now1.day, month_name, thai_year, time_str) # 30 ตุลาคม 2560 20:45:30+
    return "%d %s %d"%(now1.day, month_name, thai_year) # 30 ตุลาคม 2560 20:45:30

all_province =  [
"เชียงราย"
,"เชียงใหม่"
,"น่าน"
,"พะเยา"
,"แพร่"
,"แม่ฮ่องสอน"
,"ลำปาง"
,"ลำพูน"
,"อุตรดิตถ์"
,"กาฬสินธุ์"
,"ขอนแก่น"
,"ชัยภูมิ"
,"นครพนม"
,"นครราชสีมา"
,"บึงกาฬ"
,"บุรีรัมย์"
,"มหาสารคาม"
,"มุกดาหาร"
,"ยโสธร"
,"ร้อยเอ็ด"
,"เลย"
,"สกลนคร"
,"สุรินทร์"
,"ศรีสะเกษ"
,"หนองคาย"
,"หนองบัวลำภู"
,"อุดรธานี"
,"อุบลราชธานี"
,"อำนาจเจริญ"
,"กำแพงเพชร"
,"ชัยนาท"
,"นครนายก"
,"นครปฐม"
,"นครสวรรค์"
,"นนทบุรี"
,"ปทุมธานี"
,"พระนครศรีอยุธยา"
,"พิจิตร"
,"พิษณุโลก"
,"เพชรบูรณ์"
,"ลพบุรี"
,"สมุทรปราการ"
,"สมุทรสงคราม"
,"สมุทรสาคร"
,"สิงห์บุรี"
,"สุโขทัย"
,"สุพรรณบุรี"
,"สระบุรี"
,"อ่างทอง"
,"อุทัยธานี"
,"จันทบุรี"
,"ฉะเชิงเทรา"
,"ชลบุรี"
,"ตราด"
,"ปราจีนบุรี"
,"ระยอง"
,"สระแก้ว"
,"กาญจนบุรี"
,"ตาก"
,"ประจวบคีรีขันธ์"
,"เพชรบุรี"
,"ราชบุรี"
,"กระบี่"
,"ชุมพร"
,"ตรัง"
,"นครศรีธรรมราช"
,"นราธิวาส"
,"ปัตตานี"
,"พังงา"
,"พัทลุง"
,"ภูเก็ต"
,"ระนอง"
,"สตูล"
,"สงขลา"
,"สุราษฎร์ธานี"
,"ยะลา"
,"กรุงเทพมหานคร"
]


def match_province(text):
    res = process.extractOne(text,all_province)
    return res[0]


# def get_case_location_data(Province):
#     res = match_province(Province)
#     res = requests.get(url="https://covid,9.th-stat.com/api/open/cases/sum")
#     res = res.json()
#     return res["Province"][Province]

# res = get_case_location_data(Province="Bangkok")

    

def get_location_reccommend_data(Province):
    Province = match_province(Province)
    print(Province)
    res = requests.get(url="https://covid19.th-stat.com/api/open/area")
    res = res.json()
    
    
    
    res_cases = requests.get(url="https://covid19.th-stat.com/api/open/cases")
    res_cases = res_cases.json()
    
    data_by_case = {
        "case_num" : 0,
        "ProvinceEn" : "",
        "male" : 0,
        "female" : 0,
        "Thai" : 0,
        "Foreigner": 0,
        "latest_case": []
    }
    found = False
    for each in res_cases["Data"]:
        if each["Province"] == Province:
            data_by_case["ProvinceEn"] = each["ProvinceEn"]
            found = True
            if each["NationEn"] == "Thai":
                data_by_case["Thai"] += 1
            
            else :
                data_by_case["Foreigner"] += 1
        
            if each["GenderEn"] == "Male":
                data_by_case["male"] += 1
            
            else :
                data_by_case["female"] += 1
    
    found_area = False
    for each in res["Data"]:
        if each["Province"] == Province:
            data_by_case["case_num"] += 1
            if not found_area:
                data_by_case["ProvinceEn"] = each["ProvinceEn"]
                data_by_case["latest_case"] = each
                data_by_case["Date"] = each["Date"]
                found_area = True
            
    if found_area and found:
        Bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "carousel",
        "contents": [
        {
            "type": "bubble",
            "direction": "ltr",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
                },
                {
                "type": "text",
                "text": "Case By Location",
                "margin": "xl",
                "size": "lg",
                "align": "center",
                "weight": "bold",
                "color": "#FFFFFF"
                }
            ]
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": Province,
                        "size": "xl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": data_by_case["ProvinceEn"],
                        "margin": "none",
                        "size": "sm",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": "( รายงานผู้ติดเชื้อล่าสุด )",
                        "margin": "none",
                        "size": "sm",
                        "align": "center",
                        "weight": "regular",
                        "color": "#FF0000"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xl",
                    "contents": [
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "text",
                            "text": "ผู้ชาย",
                            "margin": "md",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["male"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "คนไทย",
                            "margin": "xl",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["Thai"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            }
                        ]
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "text",
                            "text": "ผู้หญิง",
                            "margin": "md",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["female"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "ชาวต่างชาติ",
                            "margin": "xl",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["Foreigner"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            },
            "footer": {
            "type": "box",
            "layout": "horizontal",
            "margin": "xl",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "contents": [
                    {
                    "type": "text",
                    "text": "รายงานโดย",
                    "align": "center",
                    "color": "#D4E4F6"
                    },
                    {
                    "type": "text",
                    "text": "ศูนย์ข้อมูล COVID-19 " + str(data_by_case["latest_case"]["Date"]),
                    "margin": "none",
                    "size": "sm",
                    "align": "center",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "wrap": True
                    }
                ]
                }
            ]
            },
            "styles": {
            "header": {
                "backgroundColor": "#3F72AF"
            },
            "footer": {
                "backgroundColor": "#3F72AF"
            }
            }
        },
        {
            "type": "bubble",
            "direction": "ltr",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
                },
                {
                "type": "text",
                "text": "Case By Location",
                "margin": "xl",
                "size": "lg",
                "align": "center",
                "weight": "bold",
                "color": "#FFFFFF"
                }
            ]
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": Province,
                        "size": "xl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": data_by_case["ProvinceEn"],
                        "margin": "none",
                        "size": "sm",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": "( เคสของผู้ติดเชื้อล่าสุด )",
                        "margin": "none",
                        "size": "sm",
                        "align": "center",
                        "weight": "regular",
                        "color": "#FF0000"
                        },
                        {
                        "type": "text",
                        "text": "| รายละเอียด",
                        "margin": "md",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": data_by_case["latest_case"]["Location"],
                        "margin": "none",
                        "size": "sm",
                        "align": "start",
                        "weight": "bold",
                        "color": "#000000",
                        "wrap": True
                        },
                        {
                        "type": "text",
                        "text": "| คำแนะนำ",
                        "margin": "xl",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": str(data_by_case["latest_case"]["Recommend"]).replace("<p>","").replace("<br>","").replace("</p>",""),
                        "margin": "sm",
                        "size": "sm",
                        "align": "start",
                        "weight": "bold",
                        "color": "#000000",
                        "wrap": True
                        }
                    ]
                    }
                ]
                }
            ]
            },
            "footer": {
            "type": "box",
            "layout": "horizontal",
            "margin": "xl",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "contents": [
                    {
                    "type": "text",
                    "text": "รายงานโดย",
                    "align": "center",
                    "color": "#D4E4F6"
                    },
                    {
                    "type": "text",
                    "text": "ศูนย์ข้อมูล COVID-19 "+ str(data_by_case["latest_case"]["Date"]),
                    "margin": "none",
                    "size": "sm",
                    "align": "center",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "wrap": True
                    }
                ]
                }
            ]
            },
            "styles": {
            "header": {
                "backgroundColor": "#3F72AF"
            },
            "footer": {
                "backgroundColor": "#3F72AF"
            }
            }
        }
        ]
    }
    }
        return Bubble
    
    elif found:
        Bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "carousel",
        "contents": [
        {
            "type": "bubble",
            "direction": "ltr",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
                },
                {
                "type": "text",
                "text": "Case By Location",
                "margin": "xl",
                "size": "lg",
                "align": "center",
                "weight": "bold",
                "color": "#FFFFFF"
                }
            ]
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": Province,
                        "size": "xl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": data_by_case["ProvinceEn"],
                        "margin": "none",
                        "size": "sm",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": "( รายงานผู้ติดเชื้อล่าสุด )",
                        "margin": "none",
                        "size": "sm",
                        "align": "center",
                        "weight": "regular",
                        "color": "#FF0000"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xl",
                    "contents": [
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "text",
                            "text": "ผู้ชาย",
                            "margin": "md",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["male"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "คนไทย",
                            "margin": "xl",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["Thai"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            }
                        ]
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "text",
                            "text": "ผู้หญิง",
                            "margin": "md",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["female"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "ชาวต่างชาติ",
                            "margin": "xl",
                            "size": "sm",
                            "align": "center",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": str(data_by_case["Foreigner"]),
                            "margin": "sm",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold"
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            },
            "footer": {
            "type": "box",
            "layout": "horizontal",
            "margin": "xl",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "contents": [
                    {
                    "type": "text",
                    "text": "รายงานโดย",
                    "align": "center",
                    "color": "#D4E4F6"
                    },
                    {
                    "type": "text",
                    "text": "ศูนย์ข้อมูล COVID-19 " + str(now()),
                    "margin": "none",
                    "size": "sm",
                    "align": "center",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "wrap": True
                    }
                ]
                }
            ]
            },
            "styles": {
            "header": {
                "backgroundColor": "#3F72AF"
            },
            "footer": {
                "backgroundColor": "#3F72AF"
            }
            }
        }
        ]
    }
    }
        return Bubble
    
    else:
        return False
    
res = get_location_reccommend_data(Province="กรุงเทพ")
print(res)