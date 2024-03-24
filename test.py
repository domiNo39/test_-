import os
import time

while True:
    f = open("/home/user/test/testfile.txt", 'w')
    f.write("helo word\nxoba\nbim bim bom bom")
    time.sleep(5)

