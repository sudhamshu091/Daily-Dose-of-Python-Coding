def dict_avg(list):
    for d in list:
        n1 = d.pop('CIE1')
        n2 = d.pop('CIE2')
        n3 = d.pop('CIE3')
        d['CIE1 + CIE2 + CIE3'] = (n1 + n2 + n3)/3
    return list
list = [{'id' : 91, 'subject' : 'python', 'CIE1' : 48, 'CIE2' : 48, 'CIE3':45},
 {'id' : 92, 'subject' : 'python', 'CIE1' : 46, 'CIE2' : 42, 'CIE3':44},
 {'id' : 93, 'subject' : 'python', 'CIE1' : 43, 'CIE2' : 47, 'CIE3':49}]
print(dict_avg(list))
