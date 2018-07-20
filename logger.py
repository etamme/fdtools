import curses, requests

API="http://127.0.0.1:8000"
MYCALL="K0T3ST"

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
  def __init__(self,mycall,call,band,mode):
    self.mycall=mycall
    self.call=call
    self.band=band
    self.mode=mode
    sent_rst=599
    recv_rst=599
    other=""

def logger(stdscr):
  # use kinda fake enums for band/mode to prevent data errors
  bands = Bands()
  modes = Modes()

  # setup a basic window
  wx = 20; wy = 7
  height = 5; width = 40
  win = curses.newwin(height, width, wy, wx)

  # create a new log entry and check to see if its a dupe
  log_entry = LogEntry(MYCALL,'T3ST',bands.band20,modes.cw)
  stdscr.addstr(wy,wx,'Checking '+log_entry.call)
  result = check(log_entry)
  stdscr.addstr(wy+1,wx,'T3ST:'+str(result.content))
  stdscr.addstr(wy+2,wx,'Posting '+log_entry.call)
  result = log(log_entry)
  stdscr.addstr(wy+3,wx,str(result.status_code))

  # wait for q to be pressed
  while True:
    c = stdscr.getch()
    if c == ord('q'):
      return

def check(log_entry):
  result = requests.get(API+'/check/'+log_entry.call)
  return result

def log(log_entry):
  result = requests.get(API+'/log/'+log_entry.call)
  return result

def main(): 
    curses.wrapper(logger) 
 
if __name__ == "__main__": 
    main()
