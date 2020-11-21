dict = {'Sudhamshu': '091', 'Akash': '093', 'Rajasudhan': None,'Vaishakh':'092','Naveen': 0}
new_dict = {}
for key,value in dict.items():
        if value != 0 and value is not None:
            new_dict[key] = value
print(new_dict)
