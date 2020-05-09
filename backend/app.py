import random
import time

from flask import Flask, abort, request
from flask_cors import CORS
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from BasicFunction.CaseLocationApi import get_location_reccommend_data
from BasicFunction.COVID_ANALYZER import analyze_covid_from_user
from BasicFunction.DailyApi import get_daily_data
from BasicFunction.Firebase_Connect import (delete, get, get_daily_tracking,
                                            post, post_daily_tracking, update,
                                            update_daily_tracking)
from config import Channel_access_token, Channel_secret, Firebase_DB_url , DB_COV_TRACKER , DB_USER_DATA , DB_USER_SESSION ,firebase , rich_menu_id
from FlexMessage.QuestionMsg import *
from FlexMessage.ResultMsg import *

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False
# Firebase_DB_url = "https://pybott-6th.firebaseio.com/" # Your firebase Application


from BasicFunction.api.api import get_tracking_data_by_uid , get_poll

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


@app.route("/api/get_user_report/<UID>",methods=["GET"])
def GetUserDaily(UID):
    res = get_tracking_data_by_uid(UID=UID)
    return res , 200


@app.route("/api/get_polls/")
def GetAll():
    res = get_poll()
    return res , 200
    


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # INPUT AND PARSING DATA
    REPLY_TOKEN = event.reply_token 
    MESSAGE_FROM_USER = event.message.text
    UID = event.source.user_id
    
    # get user id
    profile = line_bot_api.get_profile(UID)
    DISPLAY_NAME = profile.display_name
    PROFILE_PIC = profile.picture_url
    
    #check user in system?
    user = get(uid=UID,firebase_app=firebase , database_name=DB_USER_DATA)
    line_bot_api.link_rich_menu_to_user(user_id=UID , rich_menu_id=rich_menu_id)
    if not user:
        # continue
        data = {"session" : "None"}
        post(uid=UID,data=data,firebase_app=firebase,database_name=DB_USER_SESSION)
        
        data = { "DISPLAY_NAME" : DISPLAY_NAME , "PROFILE_PIC" : PROFILE_PIC }
        post(uid=UID,data=data,firebase_app=firebase,database_name=DB_USER_DATA)
    
    
    user_session = get(uid=UID,firebase_app=firebase , database_name=DB_USER_SESSION)
    user_session = user_session["session"]
    
    if user_session == "None":
        if MESSAGE_FROM_USER == "เริ่มบันทึกอาการป่วย":
            daily_report = {
            "มีไข้" : "",
            "มีอาการไอ" : "",
            "มีอาการเจ็บคอ" : "",
            "น้ำมูกไหล" : "",
            "เหนื่อยหอบ" : "",
            "วันที่" : "",
            "score" : 0,
            "ข้อเสนอแนะ" : "",
            "อาการอื่นๆที่พบ": ""
            }
            
            # create user daily report
            post_daily_tracking(uid=UID , data=daily_report , firebase_app=firebase , database_name=DB_COV_TRACKER)
            # update session
            
            session_data = {"session" : "บันทึกอาการไข้"}
            update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION)
            
            #Reponse กลับไปที่ห้องแชท
            Bubble = Base.get_or_new_from_json_dict(คำถามอาการไข้(),FlexSendMessage)
            line_bot_api.reply_message(REPLY_TOKEN,messages=Bubble)
        
        elif MESSAGE_FROM_USER == "ข้อมูลผู้ติดเชื้อวันนี้":
            #Reponse กลับไปที่ห้องแชท
            Bubble = Base.get_or_new_from_json_dict(get_daily_data(),FlexSendMessage)
            line_bot_api.reply_message(REPLY_TOKEN,messages=Bubble)
            
        
        elif MESSAGE_FROM_USER == "ข้อมูลผู้ติดเชื้อตามพื้นที่":
            
            session_data = {"session" : "ข้อมูลผู้ติดเชื้อตามพื้นที่"}
            update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION)
            
            line_bot_api.reply_message(REPLY_TOKEN,
                                       TextSendMessage(text="กรุณาระบุชื่อจังหวัดที่ท่านต้องการทราบคะ เช่น 'สงขลา'"))
        
        else :
            num = [1,2,3,4,5]
            time.sleep(random.choice(num))
            Fallback_list = ["น้องหมอ ยังไม่มีบริการด้านนี้นะคะ","ขออภัยคะน้องไม่เข้าใจเลยยยจีๆ","ไว้มาถามใหม่ครั้งหน้านะคะ ตอนนี้ยังไม่สะดวกคะ"]
            Fallback = random.choice(Fallback_list)
            qbtn1 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="เริ่มบันทึกอาการป่วย",text="เริ่มบันทึกอาการป่วย"))
    
            qbtn2 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                                    action=MessageAction(label="วันนี้เป็นไงบ้าง",text="ข้อมูลผู้ติดเชื้อวันนี้"))
            
            qbtn3 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="ข้อมูลผู้ติดเชื้อตามพื้นที่",text="ข้อมูลผู้ติดเชื้อตามพื้นที่"))
            
            qrep = QuickReply(items=[qbtn1,qbtn2,qbtn3])
            line_bot_api.reply_message(REPLY_TOKEN,
                                       TextSendMessage(text=Fallback,quick_reply=qrep))
    
    elif MESSAGE_FROM_USER == "ออกจากคำสั่ง":
        session_data = {"session" : "None"}
        update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION)
        num = [1,2,3,4,5]
        time.sleep(random.choice(num))
        Fallback_list = ["ออกจากคำสั่งเรียบร้อย กรุณาเลือกคำสั่งใหม่นะคะ","ออกจากคำสั่งเรียบร้อย ถามไรต่อดีเอ่ยยยย","ออกจากคำสั่งเรียบร้อย ไว้มาสอบถามใหม่อีกครั้งนะคะ","ออกจากคำสั่งเรียบร้อย ขอบคุณที่แวะมาใช้บริการนะคะ"]
        Fallback = random.choice(Fallback_list)
        qbtn1 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                        action=MessageAction(label="เริ่มบันทึกอาการป่วย",text="เริ่มบันทึกอาการป่วย"))

        qbtn2 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                                action=MessageAction(label="วันนี้เป็นไงบ้าง",text="ข้อมูลผู้ติดเชื้อวันนี้"))
        
        qbtn3 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                        action=MessageAction(label="ข้อมูลผู้ติดเชื้อตามพื้นที่",text="ข้อมูลผู้ติดเชื้อตามพื้นที่"))
        
        qrep = QuickReply(items=[qbtn1,qbtn2,qbtn3])
        line_bot_api.reply_message(REPLY_TOKEN,
                                    TextSendMessage(text=Fallback,quick_reply=qrep))
    
        
        
    ### func อื่นๆ
    else:
        if  user_session == "บันทึกอาการไข้": # validate session
                # "3" != 3
            if MESSAGE_FROM_USER in ["0","1","2","3","4","5"]: # validate input
                data = {"มีไข้" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการไอ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการไอ,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,messages=Bubble)
                
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))
        
        elif  user_session == "บันทึกอาการไอ":
            if MESSAGE_FROM_USER in ["0","1","2","3","4","5"]: # validate input
                data = {"มีอาการไอ" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการเจ็บคอ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการเจ็บคอ,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))
        
        elif  user_session == "บันทึกอาการเจ็บคอ":
            if MESSAGE_FROM_USER in ["0","1","2","3","4","5"]: # validate input
                data = {"มีอาการเจ็บคอ" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการน้ำมูกไหล"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการน้ำมูกไหล,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการน้ำมูกไหล":
            if MESSAGE_FROM_USER in ["0","1","2","3","4","5"]: # validate input
                data = {"น้ำมูกไหล" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการเหนื่อยหอบ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการเหนื่อยหอบ,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการเหนื่อยหอบ":
            if MESSAGE_FROM_USER in ["0","1","2","3","4","5"]: # validate input
                data = {"เหนื่อยหอบ" : MESSAGE_FROM_USER}
                
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการอื่นๆ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                user_daily_data = get_daily_tracking(uid=UID,firebase_app=firebase,database_name=DB_COV_TRACKER)
                result = analyze_covid_from_user(UID,user_daily_data)
                
                post_daily_tracking(uid=UID,data=result,firebase_app=firebase,database_name=DB_COV_TRACKER)
                
                qbtn = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                                        action=MessageAction(label="ไม่มีแล้วจร้า",text="ไม่มีแล้วจร้า"))
                
                qrep = QuickReply(items=[qbtn])
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("เรียบร้อยแล้วคะ🧡🧡 \n ท่านมีอาการอื่นๆเพิ่มเติมอีกไหมคะ \n 💪💪 บอกน้องหมอได้นะ",quick_reply=qrep)) # reponse
            
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการอื่นๆ":
                data = {"อาการอื่นๆที่พบ" : MESSAGE_FROM_USER}
                
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "None"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                user_daily_data = get_daily_tracking(uid=UID,firebase_app=firebase,database_name=DB_COV_TRACKER)
                result = analyze_covid_from_user(UID,user_daily_data)
                
                post_daily_tracking(uid=UID,data=result,firebase_app=firebase,database_name=DB_COV_TRACKER)
                
                raw_Bubble = GenerateResultMsg(Profile_name=DISPLAY_NAME , UserId=UID , Dict_daily_data=result)
                Bubble = Base.get_or_new_from_json_dict(raw_Bubble,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
        
        elif  user_session == "ข้อมูลผู้ติดเชื้อตามพื้นที่":
            raw_Bubble = get_location_reccommend_data(Province=MESSAGE_FROM_USER)
            if raw_Bubble:
                
                qbtn1 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="ออกจากการค้นหา",text="ออกจากคำสั่ง"))
                
                qrep = QuickReply(items=[qbtn1])
                text_message = TextSendMessage(text="ออกจากการค้นหาโดยกดปุ่มด้านล่าง หรือ ทำการค้นหาต่อไปได้เลยนะคะ" ,quick_reply=qrep)
                
                Bubble = Base.get_or_new_from_json_dict(raw_Bubble,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,messages=[Bubble,text_message])
            
            else:
                qbtn1 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="ออกจากการค้นหา",text="ออกจากคำสั่ง"))
                
                qrep = QuickReply(items=[qbtn1])
                text_message = TextSendMessage(text="ไม่พบข้อมูลผู้ติดเชื้อจากกรมควบคุมโรคของจังหวัด"+str(MESSAGE_FROM_USER) +"\n กรุณาระบุชื่อจังหวัดใหม่อีกครั้งคะ หรือ กดปุ่มออกจากการค้นหา" ,quick_reply=qrep)
                
                line_bot_api.reply_message(REPLY_TOKEN,messages=text_message)
                
            


@handler.add(FollowEvent)
def handler_Follow(event):
    UID = event.source.user_id
    REPLY_TOKEN = event.reply_token
    line_bot_api.link_rich_menu_to_user(user_id=UID , rich_menu_id="richmenu-6852c0838fd90cce0f777268248f4bb2")

    #ส่งรูปภาพ
    image_message = ImageSendMessage(
    original_content_url='https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1',
    preview_image_url='https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1'
)
    
    qbtn1 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="เริ่มบันทึกอาการป่วย",text="เริ่มบันทึกอาการป่วย"))
    
    qbtn2 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="วันนี้เป็นไงบ้าง",text="ข้อมูลผู้ติดเชื้อวันนี้"))
    
    qbtn3 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="ข้อมูลผู้ติดเชื้อตามพื้นที่",text="ข้อมูลผู้ติดเชื้อตามพื้นที่"))
    
    qrep = QuickReply(items=[qbtn1,qbtn2,qbtn3])
    text_message = TextSendMessage(text="ยินดีต้อนรับเข้าสู่ บันทึกของผู้กักตัว" ,quick_reply=qrep)
    
    line_bot_api.reply_message(REPLY_TOKEN,messages=[image_message,text_message])


if __name__ == "__main__":
    app.run()
