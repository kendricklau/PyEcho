# A script that utilizes PyEcho to send LED light
# commands through the GPIO pins on the Raspberry Pi.
# Kendrick Lau / lau21@purdue.edu / July 28, 2015

import PyEcho, getpass, time
import pigpio


RED_LED = 22
GREEN_LED = 23
BLUE_LED = 24

pi = pigpio.pi()
pi.set_mode(RED_LED, pigpio.OUTPUT)
pi.set_mode(GREEN_LED, pigpio.OUTPUT)
pi.set_mode(BLUE_LED, pigpio.OUTPUT)
STEPS = 2

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

class newTask(object):
    def __init__ (self, string):
        self.string = string

    def execute(self):
        if isinstance(self.string, basestring):
            pass

        colors = {'off': 'off', 'rain': 'rainbow', 'r': 'red', 'o': 'orange', 'y': 'yellow', 'g': 'green', 'b': 'blue', 'p': 'purple', 'w': 'white'}

        for key, value in colors.iteritems():
            if self.string.find(value) != -1:
                break

        if key == 'r':
            self.setLights(RED_LED, 255)
            self.setLights(GREEN_LED, 0)
            self.setLights(BLUE_LED, 0)
        elif key == 'o':
            self.setLights(RED_LED, 255)
            self.setLights(GREEN_LED, 153)
            self.setLights(BLUE_LED, 0)
        elif key == 'y':
            self.setLights(RED_LED, 255)
            self.setLights(GREEN_LED, 204)
            self.setLights(BLUE_LED, 0)
        elif key == 'g':
            self.setLights(RED_LED, 0)
            self.setLights(GREEN_LED, 255)
            self.setLights(BLUE_LED, 0)
        elif key == 'b':
            self.setLights(RED_LED, 0)
            self.setLights(GREEN_LED, 0)
            self.setLights(BLUE_LED, 255)
        elif key == 'p':
            self.setLights(RED_LED, 255)
            self.setLights(GREEN_LED, 0)
            self.setLights(BLUE_LED, 255)
        elif key == 'w':
            self.setLights(RED_LED, 255)
            self.setLights(GREEN_LED, 255)
            self.setLights(BLUE_LED, 255)
        elif key == 'off':
            self.offLights()

    def updateBright(self, color, step):
        color += step

        if color > 255:
            return 255
        if color < 0:
            return 0

        return color

    def setLights(self, pin, brightness):
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)

    def offLights(self):
        setLights(RED_LED, 0)
        setLights(GREEN_LED, 0)
        setLights(BLUE_LED, 0)

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
                obj = newTask(command)
                obj.execute()
                res = echo.deleteTask(task)
                if res.status_code == 200:
                    print("Task deleted")

            time.sleep(5)

if __name__ == '__main__':
    main()
    
GPIO.cleanup()
