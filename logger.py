import curses, requests

API="http://127.0.0.1:8000"

class Bands:
  def __init__(self):
    self.80m = 80
    self.40m = 40
    self.20m = 20
    self.15m = 15
    self.10m = 10
    self.6m = 6

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
  log_entry = LogEntry('T3ST',bands.20m,modes.cw)
  result = check('T3ST')
  stdscr.addstr('T3ST:'+str(result.body))

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
