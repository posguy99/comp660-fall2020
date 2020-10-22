
# if statement to check a search

spam = 'Congratulations.  You\'ve won a million dollars.'
term = input('Enter search term: ')
if term in spam:
    print('Term found!')
else:
    print('Term not found!')
