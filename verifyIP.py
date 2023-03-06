primitiveIP = "10.162.119.237"
import os
import re

ipConfig = os.popen('ipconfig').read()
currentIP = re.search(r'10\.162\.\d{0,127}\.\d{0,255}', ipConfig).group()

email_txt_ipChanged = 'IP Address has CHANGED! Analyzing domain name to a new IP...'

print('Primitive IP: ' + primitiveIP)

if currentIP != primitiveIP :
    print(email_txt_ipChanged)
else:
    print('CurrentIP: ' + currentIP + ". It's same as the primitive IP!")