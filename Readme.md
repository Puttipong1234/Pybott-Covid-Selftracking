## Source Code Pybott บันทึกของผู้กักตัว
แชทบอท + Web Application ที่เขียนด้วย Vuejs + Python Flask สำหรับการกักตัว
ของผู้ใช้งานในสถานการณ์ Covid-19 แจกจ่ายให้แก่ผู้ที่สนใจในการพัฒนา แชทบอทร่วมกับ Web platform 

### แชทบอทจากการอบรมครั้งที่ 6 
วันที่ 4-5 เมษายน ที่ผ่านมา สนใจสอบถามได้ที่ 
ส่งข้อความหน้าเพจ https://www.facebook.com/Pybott

![ScreenShot](https://scontent.fbkk22-6.fna.fbcdn.net/v/t1.0-9/93010602_553616445529371_2479078114211135488_o.png?_nc_cat=104&_nc_sid=8024bb&_nc_eui2=AeGFIQCPPcLWGfCf2YKe2FtrAwyDC345HAMDDIMLfjkcA4-LnJ9z4LairXW11rstldA&_nc_oc=AQkPmz3I_icOX7-qrAPwsHJViXePqOIq4vsBNkll91qE2aCN3Nst4nx7Qf8xxTNg87A&_nc_ht=scontent.fbkk22-6.fna&oh=afd8da579acf759c563b82f7f632d146&oe=5EDC1A80)

## วิธีการใช้งานเบื้องต้น (กรุณาศึกษา framework ก่อนเริ่มใช้งาน)
1. cmd > git clone https://github.com/Puttipong1234/Covid-SelfTracking-Pybott.git
2. สร้าง virtual env 
```
python -m venv venv (use python 3.6.8 - 3.6.10)
```
3. activate virtual evironment 
```
(window : venv\Scripts\activate / mac : source venv\bin\activate)
```
3. pip install -r requirements.txt
4. python app.py (รันแอพ)
5. deploy to heroku พร้อมตั้งค่า config local variable ต่างๆ

## หลักการ
 - frontend > เก็บไฟล์ สำหรับโปรเจค Vuejs
 - Backend > เก็บไฟล์สำหรับ Python 
 - ผู้ใช้งานควรมีความเข้าใจในการพัฒนาเว็บด้วย Flask / Vuejs 

#### ฝากติดตาม กดไลค์ กดแชร์ คอนเทน เพื่อเป็นกำลังใจแก่ทีมงานด้วยนะครับขอบพระคุณอย่างสูง