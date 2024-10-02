import os
from random import randint

# Simulating 365 days of commits
for i in range(1, 366):  # Use 366 for including the leap year
    for j in range(1, randint(1, 10)):  # Random number of commits per day
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d + '\n')  # Appending a line to the file
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "commit"')

# Push all the commits to the repository
os.system('git push -u origin main')
