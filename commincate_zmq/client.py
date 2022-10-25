import zmq

if __name__=="__main__":
	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect('tcp://127.0.0.1:6000')
	socket.send_string("Om ganesha")
	msg = socket.recv()
	print(msg)

	socket.send_string("close")
	msg = socket.recv()
	print(msg)
