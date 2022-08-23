import requests
from StockAnalysis import StockAnalysis
from StockData import StockData
from SentEmail import SentEmail
"""KEY"""
TOKEN = "56b24bb1e2cbad701eeb5b71dd3d1c5d"
PROJECT_NAME= "stockPredict"
SHEET_NAME = "stockpredict"
API_URL = f"https://api.sheety.co/{TOKEN}/{PROJECT_NAME}/{SHEET_NAME}"
USER_NAME = "quangtiennnn"
PASSWORD = 'QUANGTIENVANHUNGNGUOIBAN'
auth = (
    USER_NAME, PASSWORD
    # os.environ["USERNAME"],
    # os.environ["PASSWORD"],
)
"""GET SYMBOL FROM GOOGLE SHEET"""
response = requests.get(url=API_URL,auth = auth)
data = response.json()

"""PREDICTING STOCK USING TTI"""
n = len(data[SHEET_NAME])
for i in range(n):
    symbol = data[SHEET_NAME][i]['symbol']
    id = data[SHEET_NAME][i]['id']
    stock_data = StockData(symbol)
    stock_predict = StockAnalysis(stock_data.df).point
    API_URL_UPDATE = f"{API_URL}/{id}"
    sheet_input = stock_predict
    try:
        sheet_response = requests.put(url=API_URL_UPDATE, json=sheet_input,auth = auth)
    except:
        sheet_response = requests.post(url=API_URL, json=sheet_input,auth = auth)

"""SENDING EMAIL TO USERS"""
def get_result():
    response = requests.get(url=API_URL, auth=auth)
    data = response.json()
    results = [(data[SHEET_NAME][i]['symbol'],data[SHEET_NAME][i]['result']) for i in range(len(data[SHEET_NAME]))]
    return results
result = get_result()

"""MESSAGE"""
message = f"Today prediction: \n"
for i in range(len(result)):
    message += f"{result[i][1]}\n"

send_email = SentEmail(message)
send_email.sent_users()