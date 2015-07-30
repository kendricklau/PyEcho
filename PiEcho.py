# A script that utilizes PyEcho to send LED light
# commands through the GPIO pins on the Raspberry Pi.
# Kendrick Lau / lau21@purdue.edu / July 28, 2015

import PyEcho, getpass, time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

class parseTask(object):
    def __init__ (self, string):
        self.string = string

    def execute(self):
        if isinstance(self.string, basestring):
            pass
        colors = {'r': 'red', 'o': 'orange', 'y': 'yellow', 'g': 'green', 'b': 'blue', 'p': 'purple', 'pi': 'pink', 'w': 'white'}
        for key, value in colors.iteritems():
            if self.string.find(value) != -1:
                break
        if key == 'r':
            GPIO.output(17, GPIO.HIGH)
	    GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
	    GPIO.output(22, GPIO.LOW)
	    GPIO.output(23, GPIO.LOW)
	    GPIO.output(24, GPIO.LOW)
	    GPIO.output(10, GPIO.LOW)
	    GPIO.output(9, GPIO.LOW)	    
       	elif key == 'o':
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.LOW)
        elif key == 'y': 
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.LOW)
	elif key == 'g':
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.LOW)
	elif key == 'b':
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.LOW)
	elif key == 'p':
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.LOW)
	elif key == 'pi':
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(9, GPIO.LOW)
	elif key == 'w':
	    GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.HIGH)



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
