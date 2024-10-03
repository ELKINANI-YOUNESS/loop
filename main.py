import os
from random import randint
from datetime import datetime, timedelta

# Your GitHub username and PAT (replace 'your-username' and 'your-token' with actual values)
GITHUB_USERNAME = 'ELKINANI YOUNESS'
GITHUB_TOKEN = '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'

# Set the remote URL with PAT for authentication
REMOTE_URL = f'https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/ELKINANI-YOUNESS/loop.git'

# Update the remote origin URL with PAT
os.system(f'git remote set-url origin {REMOTE_URL}')

# Loop through the days
for i in range(1, 365):
    # Randomly determine how many commits to make on this day
    for j in range(0, randint(1, 10)):
        # Calculate the date for 'i' days ago
        d = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
        
        # Write to the file (optional, just for demonstration)
        with open('file.txt', 'a') as file:
            file.write(f'Commit on {d}\n')
        
        # Set the GIT_COMMITTER_DATE environment variable
        os.environ['GIT_COMMITTER_DATE'] = d
        
        # Git commands with the specific date
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "commit"')
    
    # Push the commits to the remote repository
    os.system('git push -u origin main')
