import os
import time

while True:
    f = open("/home/user/test/testfile.txt", 'w')
    f.write("helo word oke")
    time.sleep(5)

