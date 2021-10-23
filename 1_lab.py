mixed_list = [3, .42345, 'eras', (3+5j), '173', 65535, -391.3237162346, None, 2]

filtered_list = [x for x in mixed_list if x!=None]

tuple_list = (3, 1, .32, 'ryry', -3221.3321, None, None)

dict_list = {'int': 16768, 'float': -1.3273, 'str': 'foo_cad', 'complex': (5+1.3j), 'ept': None}

filt_dict = {key: value for key, value in dict_list.items() if len(key)>3 or value!=None}

print(filt_dict)
print(filtered_list)

def fibbon(x):
    a, b = 0, 1
    for i in range(x):
        yield a
        a, b = b, a+b

b = int(input('Is this a fibbonacci number? b= '))

print('Sure!' if b in fibbon(1000) else 'No way!')
