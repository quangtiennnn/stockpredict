import requests
from StockAnalysis import StockAnalysis
from StockData import StockData
"""KEY"""
TOKEN = "829d9b1abbddcd3cfe5512adcece5e37"
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
