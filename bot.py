import requests, time, os

TOKEN = os.environ.get("TOKEN") # راح نحط التوكن في Railway
CHANNEL = "@ahmedstore"
URL = f"https://api.telegram.org/bot{TOKEN}"

def get_price():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=10).json()
        return r['bitcoin']['usd']
    except:
        return 112000

while True:
    price = get_price()
    msg = f"سعر البيتكوين: ${price}"
    try:
        requests.get(f"{URL}/sendMessage?chat_id={CHANNEL}&text={msg}")
    except:
        pass
    time.sleep(1800) # كل 30 دقيقة
