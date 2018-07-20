import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)


# tear things down
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
