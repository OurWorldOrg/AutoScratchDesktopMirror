# Import
import requests
import os
import re

print('''
      OurWorld Auto Scratch-Desktop Mirror
      by Sunwuyuan https://wuyuan.dev
''')

# Create 'output'
if not os.path.exists('output'):
    os.mkdir('output')

# Download 'Scratch Setup.exe' for Windows
r = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch%20Setup.exe', stream=True)

with open(r'./output/scratch-win.exe', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-desktop for windows done.')

# Download 'Scratch Setup.exe' for Windows
r = requests.get('https://downloads.scratch.mit.edu/link/windows.zip', stream=True)

with open(r'./output/scratch-link-win.zip', "wb") as f:
    for chunk in r.iter_content(chunk_size=512): 
        f.write(chunk)

print('Download scratch-link for windows done.')

# Download 'Scratch.dmg' for Mac

r = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch.dmg', stream=True)

with open(r'./output/scratch-mac.dmg', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-desktop for macOS done.')

# Download 'Scratch.dmg' for Mac

r = requests.get('https://downloads.scratch.mit.edu/link/mac.zip', stream=True)

with open(r'./output/scratch-link-mac.zip', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-desktop for macOS done.')

# Get Version
try:
    getVersion = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch%20Setup.exe', allow_redirects=False)
    scratch_version = getVersion.headers['location'].split('%20')[1]
    getVersion = requests.get('https://downloads.scratch.mit.edu/link/windows.zip', allow_redirects=False)
    scratch_link_version = re.search(r"-(\d+\.\d+\.\d+)", getVersion.headers['location']).group(1)
    os.system('echo "scratch_version='+scratch_version+'-'+scratch_link_version+'" >> $GITHUB_ENV')
except:
    print('Get version Error!')
else:
    print('Get version done. version :', scratch_version+'-'+scratch_link_version, '. Cost',getVersion.elapsed.total_seconds(),'sec.')


