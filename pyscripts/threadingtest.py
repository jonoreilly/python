import threading
import time


class thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global message
        while True:
            time.sleep(1)
            message = input("input a word\n")

message = "patata"
oldmessage = None

thread1 = thread()
thread1.start()

while True:
    if message != oldmessage:
        print (message, "is delicious")
        oldmessage = message





        



