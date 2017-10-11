#!/usr/bin/env python3

import argparse

import sys
import itertools
import socket
from socket import socket as Socket

# A simple web server

# Issues:
# Ignores CRLF requirement
# Header must be < 1024 bytes
# ...
# probabaly loads more


def main():

    # Command line arguments. Use a port > 1024 by default so that we can run
    # without sudo, for use as a real server you need to use port 80.
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=2080, type=int,
                        help='Port to use')
    args = parser.parse_args()

    # Create the server socket (to handle tcp requests using ipv4), make sure
    # it is always closed by using with statement.
    #with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    ss = socket.socket()

    # The socket stays connected even after this script ends. So in order
    # to allow the immediate reuse of the socket (so that we can kill and
    # re-run the server while debugging) we set the following option. This
    # is potentially dangerous in real code: in rare cases you may get junk
    # data arriving at the socket.
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    endpoint = ('',args.port)
    ss.bind(endpoint)
    ss.listen(5)	

    print("server ready")

    while True:

         cs = ss.accept()[0] 
         request = cs.recv(1024).decode('ascii')
         reply = http_handle(request)
         cs.send(reply.encode('ascii'))


         print("\n\nReceived request")
         print("======================")
         print(request.rstrip())
         print("======================")


         print("\n\nReplied with")
         print("======================")
         print(reply.rstrip())
         print("======================")


    return 0


def http_handle(request_string):
	
	"""Given a http requst return a response
	Both request and response are unicode strings with platform standard
	line endings.
	"""

	array = request_string.split(" ")
	
	print (array [1])

	if (array[1] == "/"):
		request = "index.html"
		with open (request) as myfile:
			data = myfile.read()
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "Connection: close\n"+ "\n"
		answer = "%s%s\n" %(headers,data)
	
		return answer

	if (arreglo[1].endswith(".html")):
		request = arreglo[1][1:]
		with open(request) as myfile:
			data = myfile.read()
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "connection close\n" + "\n"
		answer = "%s%s\n"%(headers,data)
		return answer
    

	if (arreglo[1].endswith(".gif")):
		request = arreglo[1][1:]
        
		image= open(request, 'rb')
		data = image.read()
		imager = base64.encodestring(data)
		image_64_decode = base64.decodestring(imager)
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: image/gif\n" + "connection close\n" + "\n"
		answer = "%s%s\n"%(headers,imager)
		return answer
	if (arreglo[1].endswith(".gifsss")):
		request = arreglo[1][1:]
		with open(request) as myfile:
               
			data = myfile.read()
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: image/gif\n" + "connection close\n" + "\n"
		answer = "%s%s\n"%(headers,data)
		return answer
	if (arreglo[1].endswith(".js")):
		request = arreglo[1][1:]
		with open(request) as myfile:
				data = myfile.read()
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: application/javascript\n" + "connection close\n" + "\n"
		answer = "%s%s\n"%(headers,data)
		return answer
	if (arreglo[1].endswith(".css")):	
		request = arreglo[1][1:]
		with open(request) as myfile:
			data = myfile.read()
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/css\n" + "connection close\n" + "\n"
		answer = "%s%s\n"%(headers,data)
		return answer

	else :
		with open("404.html") as myfile:
				data = myfile.read()
		headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "connection close\n" + "\n"
		answer = "%s%s\n"%(headers,data)
		return answer       

    

	assert not isinstance(request_string, bytes)


    # Fill in the code to handle the http request here. You will probably want
    # to write additional functions to parse the http request into a nicer data
    # structure (eg a dict), and to easily create http responses.

    # COMPLETE (4)
    # esta funcion DEBE RETORNAR UNA CADENA que contenga el recurso (archivo)
    # que se consulta desde un navegador e.g. http://localhost:2080/index.html
    # En el ejemplo anterior se esta solicitando por el archivo 'index.html'
    # Referencias que pueden ser de utilidad
    # - https://www.acmesystems.it/python_http, muestra como enviar otros
    #                                           archivos ademas del HTML
    # - https://goo.gl/i7hJYP, muestra como construir un mensaje de respuesta
    #                          correcto en HTTP



if __name__ == "__main__":
    sys.exit(main())
