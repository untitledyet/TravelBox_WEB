phone_number = ""
sms_code = ""


import datetime

current_date = datetime.datetime.now().date()

formatted_date = current_date.strftime('%Y-%m-%d')

future_date = current_date + datetime.timedelta(days=5)
formatted_future_date = future_date.strftime('%Y-%m-%d')

print(formatted_date)
print(formatted_future_date)
