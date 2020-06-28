#!/usr/local/bin/python3
import os,sys

class _Getch:
	"""Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
	print("wootwoot")
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

wait_ctr=1;
x=61680
#for x in range(61680,62600):
while(True):
	#inny = input()
	inny = getch()
	if inny == "\x1b[A":
		x-=1
	if inny == "\x1B[B":
		x+=1	
	char_str=chr(x)
	char_blah=hex(x)
	#os.system(f"echo 'printf \"{char_blah} is {char_str}\n\"' | bash -s")
	os.system(f"xsetroot -name $(printf \"{char_blah}{char_str}\")")
	#print(f"xsetroot -name $(printf \"{char_blah} is {char_str}\")")
	#print(f"printf \"{char_str}\"")
