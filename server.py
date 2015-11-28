from BaseHTTPServer import HTTPServer

PORT_NUMBER = 8080

try:
	server = HTTPServer(('', PORT_NUMBER), http.Router)
	print 'Server listening on ', PORT_NUMBER

	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()