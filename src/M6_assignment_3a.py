
# M6 #3a

str = \
'''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# print('The input string is:\n', str)  # debug

# create a list of strings from the input
theList = str.split('\n')

# print(theList)                        # debug
count = 0
for element in theList:
    # print('Element: ', element)       # debug
    index = element.find(' :')
    if  index > -1:
        # we got here, so there's a colon in the element
        # have to test for this because split() could create empty strings
        # based on the assignment-given input

        # print(index)                  # debug

        str1 = element[index+2:]
        i = str1.find(' ')
        # print(i)                      # debug

        addr = str1[:i].rstrip()
        print('inet addr: ', addr)
        count += 1
    else:
        continue
print('Count of inet addresses: ', count)
