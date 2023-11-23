import subprocess
import os

def create_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass

# Install requirements libraries
subprocess.run('pip install -r requirements.txt', shell=True)

# Create folder and files if not exists
directories = ['./cookies', './data']
for directory in directories:
    if not os.path.exists(directory):
        os.mkdir(directory)

create_file('cookies/cookies_1.txt')
create_file('cookies/cookies_2.txt')