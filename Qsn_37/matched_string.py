import re
a = ['frame','clock','special','relativity','Sudhamshu','Rajasudhan']
text = 'Reference frames play a crucial role in special relativity theory. The term reference frame as used here is an observational perspective in space which is not undergoing any change in motion (acceleration), from which a position can be measured along 3 spatial axes (so, at rest or constant velocity). In addition, a reference frame has the ability to determine measurements of the time of events using a clock (any reference device with uniform periodicity)'
for i in a:
    if re.search(i, text):
        print('True',re.search(i,text))
    else:
        print('False')
