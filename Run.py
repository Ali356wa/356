import platform,os
arch=platform.architecture()[0]
if arch=="64bit":
  os.system('chmod +x code')
  os.system('./code')
else:print('It is a 64bit executable. Not Supported on your device.')
  
