import time, mouse, threading

diamondMined=0

for countdown in range(5):
    print("Starting in "+str(5-countdown))
    time.sleep(1)
print("Starting...", end="\n\n")

def minedIncrease():
    global diamondMined
    diamondMined+=1
    print("Diamonds mined: "+str(diamondMined))

def wait():
    time.sleep(0.1)

while True:
    mouse.drag(0, 0, 185, 30, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()
    
    mouse.drag(0, 0, -5, -200, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, 225, -5, absolute=False, duration=0.2)
    wait()
    mouse.drag(0, 0, 0, 0, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, 0, 350, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, 300, -100, absolute=False, duration=0.2)
    wait()
    mouse.drag(0, 0, 0, 0, absolute=False, duration=0.3)
    threading.Thread(target=minedIncrease).start()
    wait()

    time.sleep(5)

    mouse.drag(0, 0, 0, 0, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()
    mouse.drag(0, 0, -300, 100, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, 0, -350, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, -225, 5, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, 5, 200, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()

    mouse.drag(0, 0, -185, -30, absolute=False, duration=0.2)
    threading.Thread(target=minedIncrease).start()
    wait()
    mouse.drag(0, 0, 0, 0, absolute=False, duration=0.3)
    wait()

    time.sleep(5)
