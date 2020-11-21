import re
def date_format(date):
        return re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', '\\2-\\1-\\3', date)
date = "21-10-2020"
print("Date in mm-dd-yyyy format",date)
print("Date in dd-mm-yyyy format",date_format(date))
