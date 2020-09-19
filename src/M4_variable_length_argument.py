#!/usr/bin/env python3

# this is a cheat.  The example from Lecture 4-5 is just:
# def print_scores(score, *scores):
#     print('Test scores are:')
#     print(score)
#     for i in scores:
#         print (i)
# print_scores(10)
# print_scores(30,50,53,92)
#
# and what you get for output is:
# Test scores are:
# 10
# Test scores are:
# 30
# 50
# 53
# 92
# it is *NOT* clear what happens in the second invocation of the function
# the below modification makes it much more clear

def print_scores(score, *scores):
    print('Test scores are:')
    print('Score: ', score)
    for i in scores:
        print ('Scores: ', i)

print_scores(10)
print_scores(30,50,53,92)

# Test scores are:
# Score:  10
# Test scores are:
# Score:  30
# Scores:  50
# Scores:  53
# Scores:  92
#
# it can be seen that the first print is still being evaulated, and what is
# *actually* happening is that the variable-length argument is actually
# the "50,53,92"
# Prof Ruvalcaba does NOT explain this.
