import SimpleHTTPServer, SocketServer, MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="fdtools",
                     db="fdtools")
cur = db.cursor()

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()



def check(log):
  global cur
  cur.execute("SELECT * FROM logs WHERE dxcall="+log.dxcall+" and band="+log.band)
  if cur.rowcount() > 0:
    return "DUPE"+":"+log.dxcall+":"+log.band
  else:
    return "NODUPE"+":"+log.dxcall+":"+log.band

def log(log):
  return ""
