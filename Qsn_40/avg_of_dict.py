def avg(cie):
    dict={}
    for key,value in cie.items():
        if key=='cie1':
            dict[key]=value
        elif key=='cie2':
            dict[key]=value
        elif key=='cie3':
            dict[key]=value
            return sum(dict.values())/len(dict)
def pick_except(cie):
    dict1={}
    for key,value in cie.items():
        if key=='cie1':
            pass
        elif key=='cie2':
            pass
        elif key=='cie3':
            pass
        else:
            dict1[key]=value
    return dict1

cie={'id':91,'subject':'python','cie1':48,'cie2':48,'cie3':45}
avg_cie=pick_except(cie)
avg_cie['cie1+cie2+cie3']=avg(cie)
print(avg_cie)
