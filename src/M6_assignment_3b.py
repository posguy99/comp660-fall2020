
# M6 #3b

str = \
'''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# print('The input string is:\n', str)  # debug

count = str.count('inet addr')

print('Count of inet addresses: ', count)
