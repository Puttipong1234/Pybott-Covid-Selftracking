Channel_access_token = "Your_Token"
Channel_secret = "Your_Token"
Firebase_DB_url = "Your Database Url"
rich_menu_id = "Your_Richmenu_Id"

from firebase import firebase
firebase = firebase.FirebaseApplication(Firebase_DB_url, None)
DB_COV_TRACKER = "COV_TRACKER"
DB_USER_SESSION = "USER_SESSION"
DB_USER_DATA = "USER_DATA"