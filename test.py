import os
import time

while True:
    f = open("/home/user/test/testfile.txt", 'w')
    f.write("helo word")
    time.sleep(5)

