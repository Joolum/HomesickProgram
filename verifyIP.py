primitiveIP = "10.162.119.237"
import os
import re

ipconfig = os.popen('ipconfig').read()
currentIP = re.search(r'10\.162\.\d{0,127}\.\d{0,255}', ipconfig).group()

if currentIP != primitiveIP :
    print('IP Address has CHANGED! Analyzing domain name to a new IP...')
else:
    print('CurrentIP: ' + currentIP + ". It's same as primitive IP!")