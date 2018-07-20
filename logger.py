import curses, requests

API="http://127.0.0.1:8000"

class Bands:
  def __init__(self):
    self.band80 = 80
    self.band40 = 40
    self.band20 = 20
    self.band15 = 15
    self.band10 = 10
    self.band6 = 6

class Modes:
  def __init__(self):
    self.cw = "cw"
    self.ssb = "ssb"
    self.ft8 = "ft8"
    self.lsat = "lsat"
    self.fsat = "fsat"

class LogEntry:
  def __init__(self,call,band,mode):
    self.call=call
    self.band=band
    self.mode=mode

def logger(stdscr):
  # use kinda fake enums for band/mode to prevent data errors
  bands = Bands()
  modes = Modes()

  # setup a basic window
  begin_x = 20; begin_y = 7
  height = 5; width = 40
  win = curses.newwin(height, width, begin_y, begin_x)

  # create a new log entry and check to see if its a dupe
  log_entry = LogEntry('T3ST',bands.band20,modes.cw)
  result = check(log_entry)
  stdscr.addstr('T3ST:'+str(result.content))

  # wait for q to be pressed
  while True:
    c = stdscr.getch()
    if c == ord('q'):
      return

def check(log):
  result = requests.get(API+'/check/'+log.call)
  return result

def main(): 
    curses.wrapper(logger) 
 
if __name__ == "__main__": 
    main()
