import smtplib
import requests

"""KEY FOR API REQUEST"""
TOKEN = "56b24bb1e2cbad701eeb5b71dd3d1c5d"
PROJECT_NAME = "stockPredict"
SHEET_NAME = "users"
API_URL = f"https://api.sheety.co/{TOKEN}/{PROJECT_NAME}/{SHEET_NAME}"
USER_NAME = "quangtiennnn"
PASSWORD = 'QUANGTIENVANHUNGNGUOIBAN'
auth = (
    USER_NAME, PASSWORD
    # os.environ["USERNAME"],
    # os.environ["PASSWORD"],
)
"""KEY FOR MAIL"""
MY_EMAIL = "darknexnguyen2000@gmail.com"
PASSWORD = "wnolsupvripgehiq"


class SentEmail:
    def __init__(self, message: str):
        self.users_mail = self.get_users_mail()
        self.message = message

    def get_users_mail(self):
        response = requests.get(url=API_URL, auth=auth)
        data = response.json()
        users_mail = [data[SHEET_NAME][i]['email'] for i in range(len(data[SHEET_NAME]))]
        return users_mail

    def sent_users(self):
        text = f"Subject: Stock Prediction 1.0\n{self.message}"
        for user_email in self.users_mail:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=user_email, msg=text)
            connection.close()
