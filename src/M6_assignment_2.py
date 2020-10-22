
# M6 #2

str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

index = str.find(':')
if index > 0:
    # clip off the front
    str1 = str[index+1:]
    i = str1.find(' ')
    addr = str1[:i].rstrip()
    # addr is the inet address
    print('Address: ', addr)
