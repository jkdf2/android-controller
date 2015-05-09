from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
from time import sleep
import signal

def execute():
    height = int(device.getProperty('display.height'))
    y1 = int(height * (0.75))
    y2 = int(height * (0.50))

    width = int(device.getProperty('display.width'))
    x = int(width * (0.50))

    dragLength = 0.05
    longDragTouches = 100
    shortDragTouches = longDragTouches / 10

    print "Scrolling upwards for infinity. CTRL + C to exit."

    index = 0
    while valid:
        device.drag((x, y2), (x, y1), dragLength, longDragTouches)
        index += 1
        if (x % 50 == 0): #sometimes scrolling infinitely in one direction freezes
            device.drag((x, y1 + 50), (x, y1), dragLength, shortDragTouches)
        sleep(0.2) #give exit time to process

def exitGracefully(signum, frame):
    print 'you pressed ctrl + c'
    device.shell('killall com.android.commands.monkey')
    sys.exit(0)

if __name__ == '__main__':
    global device
    global valid
    valid = True
    device = MonkeyRunner.waitForConnection() 
    signal.signal(signal.SIGINT, exitGracefully)
    execute()
