import time

class countdown():
    def __init__(self):
        pass
    
    def start(self, count):
        for countdown in range(count):
            print("Starting in "+str(count-countdown))
            time.sleep(1)
        print("Starting...", end="\n\n")
