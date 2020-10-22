
# term in string

spam = 'Congratulations.  You\'ve won a million dollars.'
print('million' in spam)        # true
print('Million' in spam)        # false
print('on' in spam)             # true
print(' million ' in spam)      # true
print(' dollars ' in spam)      # false
