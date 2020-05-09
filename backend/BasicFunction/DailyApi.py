import requests

def get_daily_data():
    res = requests.get(url="https://covid19.th-stat.com/api/open/today")
    res = res.json()
    
    
    bubble = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
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
          "text": "Daily Report",
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
              "type": "text",
              "text": "ข้อมูลประจำวัน",
              "size": "xl",
              "align": "center",
              "weight": "bold",
              "color": "#3F72AF"
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
                      "text": "ติดเชื้อ",
                      "margin": "md",
                      "size": "md",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": str(res["Confirmed"]),
                      "margin": "sm",
                      "size": "lg",
                      "align": "center",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "( +" + str(res["NewConfirmed"]) +" )" if res["NewConfirmed"] >= 0 else "( " + str(res["NewConfirmed"]) +" )",
                      "margin": "none",
                      "size": "xs",
                      "align": "center",
                      "weight": "regular",
                      "color": "#009032" if res["NewConfirmed"] >= 0 else "#FF0000"
                    },
                    {
                      "type": "text",
                      "text": "เสียชีวิต",
                      "margin": "xl",
                      "size": "md",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": str(res["Deaths"]),
                      "margin": "sm",
                      "size": "lg",
                      "align": "center",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "( +" + str(res["NewDeaths"]) +" )" if res["NewDeaths"] >= 0 else "( " + str(res["NewDeaths"]) +" )",
                      "margin": "none",
                      "size": "xs",
                      "align": "center",
                      "weight": "regular",
                      "color": "#009032" if res["NewDeaths"] >= 0 else "#FF0000"
                    },
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "หายแล้ว",
                      "margin": "md",
                      "size": "md",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": str(res["Recovered"]),
                      "margin": "sm",
                      "size": "lg",
                      "align": "center",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text":  "( +" + str(res["NewRecovered"]) +" )" if res["NewRecovered"] >= 0 else "( " + str(res["NewRecovered"]) +" )",
                      "margin": "none",
                      "size": "xs",
                      "align": "center",
                      "weight": "regular",
                      "color": "#009032" if res["NewRecovered"] >= 0 else "#FF0000"
                    },
                    {
                      "type": "text",
                      "text": "กำลังรักษา",
                      "margin": "xl",
                      "size": "md",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": str(res["Hospitalized"]),
                      "margin": "sm",
                      "size": "lg",
                      "align": "center",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "( +" + str(res["NewHospitalized"]) +" )" if res["NewHospitalized"] >= 0 else "( " + str(res["NewHospitalized"]) +" )",
                      "margin": "none",
                      "size": "xs",
                      "align": "center",
                      "weight": "regular",
                      "color": "#009032" if res["NewHospitalized"] >= 0 else "#FF0000"
                    },
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
              "text": "ข้อมูลจากกรมควบคุมโรค",
              "margin": "xl",
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
}
    

    return bubble



