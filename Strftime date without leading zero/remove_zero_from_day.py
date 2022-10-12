from datetime import datetime, date

date_ip= "2022-08-02"
date_time = datetime.strptime(date_ip, "%Y-%m-%d")

date_without_zero = date_time.strftime("%d-%m-%Y").lstrip('0')

print("date without any formatting: ",date_time)
print("The Date without zero in day is: ", date_without_zero)