#!/usr/bin/env python3

total_score = 0
for i in range(3):
    while True:
        score = int(input('Enter test score: '))
        if score >= 0 and score <= 100:
            total_score += score
            break
        else:
            print('Test score must be between 0 and 100.')
print('Test score: ', total_score)
