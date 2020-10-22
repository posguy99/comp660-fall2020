
message = "Hello Python!"
print(len(message))         # 13


message = 'Hello Python!'
print(message[0])           # H
print(message[1])           # e
print(message[-1])          # !
print(message[16])          # IndexError: 'string index out of range'
message[0] = 'J'            # TypeError: "'str' object does not support item assignment"
