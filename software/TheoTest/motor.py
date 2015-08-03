import curses
import mraa
import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,0,"Press 'q' to quit\n")
stdscr.refresh()


def set_motor(chan,en,phase):
	if(chan == 0):
		gpio = mraa.Gpio(21)
		gpio.dir(mraa.DIR_OUT)
		gpio.write(phase)
		gpio = mraa.Gpio(0)
		gpio.dir(mraa.DIR_OUT)
		gpio.write(en)
	elif(chan == 1):
		gpio = mraa.Gpio(20)
		gpio.dir(mraa.DIR_OUT)
		gpio.write(phase)
		gpio = mraa.Gpio(14)
		gpio.dir(mraa.DIR_OUT)
		gpio.write(en)
	

def init_motor():
	gpio = mraa.Gpio(31)
	gpio.dir(mraa.DIR_OUT)
	gpio.write(1)
	# setting motor to run in Enable/Phase mode

	set_motor(0,0,0)
	set_motor(1,0,0)

def move_forward():
	set_motor(0,1,0)
	set_motor(1,0,0)

def move_backward():
	set_motor(0,1,1)
	set_motor(1,0,0)

def turn_left():
	set_motor(0,0,0)
	set_motor(1,1,0)

def turn_right():
	set_motor(0,0,0)
	set_motor(1,1,1)

def updateMotor(key):
	if(key==ord('w') or key==curses.KEY_UP):
		stdscr.addstr(1,0,"Forward ")
		move_forward()
	elif(key==ord('s') or key==curses.KEY_DOWN):
		stdscr.addstr(1,0,"Backward")
		move_backward()
	elif(key==ord('a') or key==curses.KEY_LEFT):
		stdscr.addstr(1,0,"Left    ")
		turn_left()
	elif(key==ord('d') or key==curses.KEY_RIGHT):
		stdscr.addstr(1,0,"Righ    ")
		turn_right()
	elif(key==ord(' ')):
		stdscr.addstr(1,0,"Stop    ")
		init_motor()

init_motor()

key = ''
while key != ord('q'):
	key = stdscr.getch()
	#stdscr.addch(1,2,key)
	#stdscr.refresh()
	updateMotor(key)

curses.endwin()

