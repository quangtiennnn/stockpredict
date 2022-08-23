import requests
import datetime as dt

TOKEN = "829d9b1abbddcd3cfe5512adcece5e37"
PROJECT_NAME= "stockPredict"
SHEET_NAME = "users"
API_URL = f"https://api.sheety.co/{TOKEN}/{PROJECT_NAME}/{SHEET_NAME}"
USER_NAME = "quangtiennnn"
PASSWORD = 'QUANGTIENVANHUNGNGUOIBAN'
auth = (
    USER_NAME, PASSWORD
    # os.environ["USERNAME"],
    # os.environ["PASSWORD"],
)

current = dt.datetime.now()
current_day = current.strftime("%d/%m/%Y")
print("Halo welcome to Stock Prediction 1.0 made by quangtiennnn!! Register for daily alert!!\n")
name = input("Your name: ").title()
email = input("Your email: ")

sheet_input = {
    'user': {
        'date': current_day,
        'name': name,
        'email':email,
    }
}
sheet_response = requests.post(url=API_URL, json=sheet_input,auth = auth)