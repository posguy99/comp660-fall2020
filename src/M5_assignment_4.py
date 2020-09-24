
# 4. Explain what happens when the following recursive functions is called
# with the value “alucard” and 0 as arguments:


def semordnilap(aString, index):
    ''' Print palindromes (reversed text strings)
        aString = string to print reversed
        index = position to start printing from
    '''
    if index < len(aString):
        semordnilap(aString, index + 1)
        print(aString[index], end="")


def main():
    print('Test case')
    print('Should print the string "dracula"')
    semordnilap('alucard', 0)


if __name__ == "__main__":
    main()
