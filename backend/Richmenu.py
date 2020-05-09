richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "> เมนูหลัก <",
  "areas": [
    {
      "bounds": {
        "x": 39,
        "y": 39,
        "width": 1550,
        "height": 785
      },
      "action": {
        "type": "message",
        "text": "เริ่มบันทึกอาการป่วย"
      }
    },
    {
      "bounds": {
        "x": 1638,
        "y": 39,
        "width": 804,
        "height": 785
      },
      "action": {
        "type": "uri",
        "uri": 'https://liff.line.me/1654070318-rlnJ7Rpn'
      }
    },
    {
      "bounds": {
        "x": 48,
        "y": 875,
        "width": 727,
        "height": 737
      },
      "action": {
        "type": "message",
        "text": "ข้อมูลผู้ติดเชื้อวันนี้"
      }
    },
    {
      "bounds": {
        "x": 814,
        "y": 866,
        "width": 765,
        "height": 775
      },
      "action": {
        "type": "message",
        "text": "ข้อมูลผู้ติดเชื้อตามพื้นที่"
      }
    },
    {
      "bounds": {
        "x": 1638,
        "y": 875,
        "width": 814,
        "height": 766
      },
      "action": {
        "type": "uri",
        "uri": 'https://liff.line.me/1654070318-rlnJ7Rpn'
      }
    }
  ]
}


from config import Channel_access_token #
channel_access_token = Channel_access_token
Image_File_Path = "Material\\richmenu.png"
import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())


CreateRichMenu(ImageFilePath=Image_File_Path,Rich_json=richdata,channel_access_token=channel_access_token)