def date_format(date):
    a = date.split("-")
    a[0],a[1] = a[1],a[0]
    print("Date in mm-dd-yyyy format is:"+a[0]+"-"+a[1]+"-"+a[2])
date = "21-10-2000"
print("Date in dd-mm-yyyy format is:"+date)
date_format(date)
