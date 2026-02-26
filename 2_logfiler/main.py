import re
from pathlib import Path


data_dir = Path.cwd() / 'logfiler'
logfile = 'app_log (logfil analyse) - random.txt'

# Load logfile

with open(data_dir / logfile, 'r') as f:
    lines = f.readlines()


# Extract different types of log message
# det dur vist ikke at den også putter terror ind under error

log_messages: dict = {'warning': [], 'error': [], 'info': [], 'success': [], 'notice': []}

for line in lines:
#    words = line.lower().split()
    for key, message in log_messages.items():
        if key in line.lower():
            message.append(line)
        continue

# Make new file for each log message type

output_dir = data_dir / f'logs_{logfile.split('.')[0]}'
Path(output_dir).mkdir(exist_ok=True)

for key, message in log_messages.items():
    if not message:
        continue
    filename = f'{key}.log'
    with open(output_dir / filename, 'w') as f:
        f.writelines(message)

