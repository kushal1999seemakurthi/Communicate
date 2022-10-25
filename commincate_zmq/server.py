import zmq

if __name__=="__main__":
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind('tcp://127.0.0.1:6000')
	while True:
		msg = socket.recv()
		print(msg)
		msg = msg.decode()
		print(msg)
		if msg == 'zeromq':
			socket.send_string('ah ha! you got it')
		elif msg!= "close":
			socket.send_string(msg)
		else:
			socket.send_string("Socket is closing")
			socket.close()
			break
	print("Server is stopped")

