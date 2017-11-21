#!/usr/bin/env python
import time
import os

timeout = time.time() + 60*1
def curl_write():
    start_time = time.time()
    os.system("curl http://localhost:8080 &> /dev/null")
    print("%s\n" % (time.time() - start_time))
    with open("get_time", mode='a') as file:
        file.write("%s\n" % (time.time() - start_time))
    return;

while True:
    curl_write()
    if time.time() > timeout:
        os._exit(0)
        break
