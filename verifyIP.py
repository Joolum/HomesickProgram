primitiveID = "10.162.119.237"
import os
import re

ipconfig = os.popen('ipconfig').read()
ip = re.search(r'10\.162\.\d{0,127}\.\d{0,255}', ipconfig).group()

print(ip)