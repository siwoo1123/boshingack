import time

while True:
    print(time.strftime('%Z %Y %m %d %p %I %M %S', time.localtime(time.time())))
    time.sleep(1)