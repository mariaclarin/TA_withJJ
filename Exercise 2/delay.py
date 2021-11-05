import time
def delay (msg, sec) :
    x = str(msg)
    t = time.sleep(sec) 
    print(x)

delay("This is message", 5)