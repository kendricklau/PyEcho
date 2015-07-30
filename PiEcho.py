# A script that utilizes PyEcho to send LED light
# commands through the GPIO pins on the Raspberry Pi.
# Kendrick Lau / lau21@purdue.edu / July 28, 2015

import PyEcho, getpass, time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

class sendGPIO(object):
    def __init__(self, gpiolist = []):
        self.gpiolist = gpiolist

    def trueGPIO(self):
        allgpio = [17,18,27,22,23,24,10,9,25,11,8,7]

        for n in allgpio:
            try:
	        if self.gpiolist.index(n) != -1:
		    GPIO.output(n, GPIO.HIGH)
	    except ValueError:
		GPIO.output(n, GPIO.LOW)

class parseTask(object):
    def __init__ (self, string):
        self.string = string

    def execute(self):
        if isinstance(self.string, basestring):
            pass

        colors = {'rain': 'rainbow', 'r': 'red', 'o': 'orange', 'y': 'yellow', 'g': 'green', 'b': 'blue', 'p': 'purple', 'pi': 'pink', 'w': 'white'}

        for key, value in colors.iteritems():
            if self.string.find(value) != -1:
                break

        if key == 'r':
            command = sendGPIO([17])
            command.trueGPIO()
       	elif key == 'o':
	    command = sendGPIO([18])
            command.trueGPIO()
        elif key == 'y': 
	    command = sendGPIO([25])
            command.trueGPIO()
	elif key == 'g':
	    command = sendGPIO([22])
            command.trueGPIO()
	elif key == 'b':
            command = sendGPIO([23])
            command.trueGPIO()
	elif key == 'p':
	    command = sendGPIO([24])
            command.trueGPIO()
	elif key == 'pi':
            command = sendGPIO([10])
            command.trueGPIO()
	elif key == 'w':
	    command = sendGPIO([9])
            command.trueGPIO()
    	elif key == 'rain':
            while(True):
                command = sendGPIO([17])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([18])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([25])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([22])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([23])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([24])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([10])
                command.trueGPIO()
                time.sleep(.05)
                command = sendGPIO([9])
                command.trueGPIO()
                time.sleep(.05)
		if echo.tasks() != 0:
		    break


def main():
    email = raw_input("Email: ")
    print("If using IDLE, getpass will display RAW PASSWORD.")
    password = getpass.getpass()
    echo  = PyEcho.PyEcho(email, password)
    if echo:
        while True:
            tasks = echo.tasks()
            for task in tasks:
                command = task['text']
                print("Task: " + command)
                obj = parseTask(command)
                obj.execute()
                res = echo.deleteTask(task)
                if res.status_code == 200:
                    print("Task deleted")

            time.sleep(5)

if __name__ == '__main__':
    main()
    
GPIO.cleanup()
