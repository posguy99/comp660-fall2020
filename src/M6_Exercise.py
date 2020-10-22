
# string traversal

fruit = 'Apple'

# print forwards

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# exercise 1 - print in reverse

index = len(fruit)
while index:
    letter = fruit[index - 1]   # because slice is zero-based
    print(letter)
    index = index - 1

# exercise 2 - what is [:]

print(fruit[:])

# exercise 3 -


def countem(word, char):
    count = 0
    for i in range(len(word)):
        if word[i] == char:
            count = count + 1
    return count

print(countem(fruit, 'p'))


# **Exercise 4: There is a string method called count that is similar to the
# function in the previous exercise. Read the documentation of this method at:
# Write an invocation that counts the number of times the letter a occurs in
# “banana”.*

print(fruit.count('p'))


# exercise 5 -

str = 'X-DSPAM-Confidence:0.8475'
loc = int(str.find(':')) + 1        # get to char after the colon
score = float(str[loc : ])          # from  after the colon to the end
print('score: ', score)
