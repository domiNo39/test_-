import os
import time

while True:
    f = open("testfile.txt", 'w')
    f.write("helo")
    time.sleep(5)

