from datetime import datetime, date

date_ip= "2022-08-10"

date_time = datetime.strptime(date_ip, "%Y-%m-%d")

date_without_zero = date_time.strftime('X%d-X%m-%Y').replace('X0','X').replace('X','')
print("date without any formatting: ",date_time)
print("The Date without zero in Month and day is: ", date_without_zero)