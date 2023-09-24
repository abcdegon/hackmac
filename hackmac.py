#!/usr/bin/enc python
import curses
from curses import wrapper

def main(stdscr):
    min = 0
    max = 0
    c = 1


    h = 7
    w = 32
    y = int( (curses.LINES-11)/2 )
    x = int( (curses.COLS-32)/2 )
    stdscr.clear()
    win = curses.newwin(h,w,y,x)

    while c > max:
        win.clear()
        win.border()
        win.addstr(1,8,"Abcds Hackmac")
        win.hline(2,1,0,30)
        win.addstr(3,5,"Exit ............ [0]")
        win.hline(4,1,0,30)
        win.addstr(5,5,"Your choice [{},{}]".format(min,max))
        z=win.getstr(5,23)
        win.refresh()
        try:
            c=int(z)
        except:
            win.clear()
            win.addstr(1,1,"Please enter a valid integer.")
            win.getch()
            win.refresh()


if __name__ == "__main__" :
    wrapper(main)

