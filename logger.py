import curses
# setup curses and the terminal

def logger(stdscr):
  begin_x = 20; begin_y = 7
  height = 5; width = 40
  win = curses.newwin(height, width, begin_y, begin_x)


def main(): 
    curses.wrapper(logger) 
 
if __name__ == "__main__": 
    main()
