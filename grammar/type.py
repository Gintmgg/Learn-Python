# -*- coding: utf-8 -*- 

intA = 1
floatB = 0.1

print '\tintA => {0}\n\tfloatB => {1}'.format(intA, floatB)

my_arr = ['a', 'b', 'c']

strA = 'abc'

strB = '1233abcde'

if strA in strB:
    print 'strA in strB'
else:
    print 'strA not in strB'

for item in my_arr:
    print 'item => {0}'.format(item)

for item in range(len(my_arr)):
    print 'item => {0}'.format(item)

my_dict = {'my':123, 'self': 567}

print 'my_dict {0}'.format(my_dict)

for k in my_dict.keys():
    print 'key [ %s ]' % k

for v in my_dict.values():
    print 'value {0}'.format(v)

for k,v in my_dict.items():
    print 'key [ %s ], value [ %s ]' %(k, v)
