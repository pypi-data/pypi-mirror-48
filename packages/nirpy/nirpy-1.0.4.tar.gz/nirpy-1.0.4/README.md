<br>

![Python](https://www.python.org/static/img/python-logo@2x.png)

# `pip install nirpy`

<br>

> Example usage:
```
import nirpy
nirpy.load()
nirpy.execute('monitor off/on') # Disable/Enable monitor
nirpy.execute('savescreenshotfull photo.png') # Desktop screenshot
nirpy.execute('cdrom open/close') # cdrom Open/Close
nirpy.execute('emptybin') # Empty trashbin
nirpy.execute('speak text Hello World!') # Speak text
nirpy.unload()
```

<br>
Wait until all commands are executed and continue to execute your code:<br>
nirpy.execute('infobox \"Computer will restart\" \"INFO\" && shutdown.exe -r -t 0', wait=True)<br>
<br>
Wait until command are executed with high process priority and continue to execute your code.<br>
Process priority list: [LOW | NORMAL | HIGH | REALTIME]<br>
nirpy.execute('savescreenshotfull desktop.png', wait=True, priority='HIGH')<br>
<br>
Download file from internet:<br>
file = nirpy.wget(link)<br>
<br>
Execute downloaded file:<br>
nirpy.start(file) or nirpy.start('filename.txt')<br>
<br>
Extract file from archive:<br>
nirpy.unzip('test.zip', 'file.exe')<br>
<br>
Add file to archive:<br>
nirpy.addzip('test.zip', 'file.exe')<br>
<br>

## After executing you can use: nirpy.unload() to remove nircmdc.exe from system.

*nircmdc download : https://www.nirsoft.net/utils/nircmd.html* <br>
*nircmdc reference: https://nircmd.nirsoft.net* <br>
![SITE](https://i.ibb.co/znRLN0D/image.png)

<br>

[Module Created by LimerBoy with Love <3](https://www.youtube.com/channel/UCtgsa9eFPLCldJwPfXwmZaw?view_as=subscriber)

<br>
