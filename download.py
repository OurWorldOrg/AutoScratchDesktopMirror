# Import
import requests
import os

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

# Get Scratch Version
try:
    getVersion = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch%20Setup.exe', allow_redirects=False)
    version = getVersion.headers['location'].split('%20')[1]
    os.system('echo "scratch_version='+version+'" >> $GITHUB_ENV')
except:
    print('Get version Error!')
else:
    print('Get version done. version :', version, '. Cost',getVersion.elapsed.total_seconds(),'sec.')


# Get Scratch link Version
try:
    getVersion = requests.get('https://downloads.scratch.mit.edu/link/windows.zip', allow_redirects=False)
    version = getVersion.headers['location'].split('%20')[1]
    os.system('echo "scratch_link_version='+version+'" >> $GITHUB_ENV')
except:
    print('Get link version Error!')
else:
    print('Get link version done. link version :', version, '. Cost',getVersion.elapsed.total_seconds(),'sec.')

