import datetime
todays_date = datetime.date.today()
print("Today's date:",todays_date)

new_date = datetime.date.strftime(todays_date, "%m/%d/%Y")
print("Date in mmddyyyy format:", new_date)
new_date = datetime.date.strftime(todays_date, "%d/%m/%Y")
print("Date in ddmmyyyy format:", new_date)
