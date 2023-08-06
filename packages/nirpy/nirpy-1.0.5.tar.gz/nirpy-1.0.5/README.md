<br>

![Python](https://www.python.org/static/img/python-logo@2x.png)

# `pip install nirpy`

<br>

> Example usage:
```
# Import this module
import nirpy

# Load nircmdc.exe to system
nirpy.load() # if system 64 bit: nirpy.load(architecture=64)

# NIRCMDC.exe commands:
nirpy.execute('monitor off/on') # Disable/Enable monitor
nirpy.execute('savescreenshotfull photo.png') # Desktop screenshot
nirpy.execute('cdrom open/close') # cdrom Open/Close
nirpy.execute('emptybin') # Empty trashbin
nirpy.execute('speak text Hello World!') # Speak text

# CMD.exe commands:
nirpy.system('echo It works!')

# Clean nirpy cache
nirpy.clean()

# Remove nircmdc.exe from system
nirpy.unload()
```

<br>
#Execute with high process priority<br>
#Process priority: [LOW | NORMAL | HIGH | REALTIME]<br>
nirpy.execute('savescreenshotfull desktop.png', priority='HIGH')<br>
<br>
Download file from internet:<br>
file = nirpy.wget(link)<br>
<br>
Execute downloaded file:<br>
nirpy.start(file) or nirpy.start('filename.txt')<br>

<br>
Add/Remove autorun<br>
nirpy.autorun('C:\\Windows', 'notepad.exe', 'test_name', state=True) # Add notepad to startup<br>
nirpy.autorun('C:\\Windows', 'notepad.exe', 'test_name', state=False) # Remove notepad from startup<br>



*nircmdc download : https://www.nirsoft.net/utils/nircmd.html* <br>
*nircmdc reference: https://nircmd.nirsoft.net* <br>
![SITE](https://i.ibb.co/znRLN0D/image.png)

<br>

[Module Created by LimerBoy with Love <3](https://www.youtube.com/channel/UCtgsa9eFPLCldJwPfXwmZaw?view_as=subscriber)

<br>
