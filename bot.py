import requests
import json
import time
from datetime import date
from datetime import timedelta

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
while(1):
    welcome = "https://api.telegram.org/bot1860762680:AAESCF3W8Kcb6dfUkZISTjz7UUSx5n7Q6e4/sendMessage?chat_id=-1001392556159&text=Hello i am Sourabh,developed by anonymous ,i will send real time covid vaccine availability slot notification for the district of Narsingpur,notification will be send after every 15 minutes"
    requests.get(welcome)
    msg = []
    today = date.today()+timedelta(days=1)
    day = today.strftime("%d-%m-%Y")

    x = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=487551&date="+day
    # x="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=462001&date="+day
    print(x)
    data = requests.get(x, headers=headers)
    print(data)
    results = json.loads(data.text)
    count = results["sessions"]
    
    if(len(count) > 0):
        slot_available = True
        for session in count:
            if (session["available_capacity"] > 0):
                msg = []
                msg.append({"Pincode": session["pincode"], "1": session["name"], "vaccine": session["vaccine"],
                        "availability": session["available_capacity"], "min-age": session["min_age_limit"], "date": session["date"]})
                parse_data = json.dumps(msg)
                parse_data = parse_data.replace('"', "")
                parse_data = parse_data.replace("{", "")
                parse_data = parse_data.replace("}", "\n")
                parse_data = parse_data.replace("[", "")
                parse_data = parse_data.replace("]", "")
                parse_data = parse_data.replace(",", "\n")
                # parse_data=parse_data.replace(":","-")
                print(parse_data)
                # welcome1="https://api.telegram.org/bot1860762680:AAESCF3W8Kcb6dfUkZISTjz7UUSx5n7Q6e4/sendMessage?chat_id=-1001392556159&text=Notification for: "+session["district_name"]
                # requests.get(welcome1)
                nd_url = "https://api.telegram.org/bot1860762680:AAESCF3W8Kcb6dfUkZISTjz7UUSx5n7Q6e4/sendMessage?chat_id=-1001392556159&text="+parse_data
                y = requests.get(nd_url)
                print(y)
        time.sleep(8)
