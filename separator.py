import os
import shutil

logsdir = "logs\\"
files = os.listdir(logsdir)

# Create Directory
if not os.path.exists('separated/anomalous'):
    os.makedirs('separated/anomalous')

if not os.path.exists('separated/normal'):
    os.makedirs('separated/normal')

destination_anomalous = "separated/anomalous"
destination_normal = "separated/normal"

for file in files:
    if not file.endswith('.log'):
        shutil.copy(logsdir + file, destination_anomalous)
    else:
        shutil.copy(logsdir + file, destination_normal)
