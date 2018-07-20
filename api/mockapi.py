import SimpleHTTPServer, SocketServer, MySQLdb

#db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                     user="user",         # your username
#                     passwd="pass",  # your password
#                     db="fdlog")        # name of the data base


PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()



#def check(log_entry):
#  return ""

#def log(log_entry):
#  return ""
