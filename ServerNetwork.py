import socket
import threading

class NetworkConnector():
  def __init__(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.host = socket.gethostname()
    self.port = 9999
    self.sock.bind((self.host, self.port))
    self.sock.listen(5)
    self.conns = []

  def clientthread(self, conn):
    while True:
      msg = conn.recv(1024).decode("utf-8")
      print("message received from " + self.addr[0] + " on " + str(self.addr[1]) + ": " + msg)
      self.broadcast(msg)
    
  def broadcast(self, msg):
    print(self.conns)
    for conn in self.conns:
      conn.sendall(msg.encode("utf-8"))
  
  def waitforclients(self):
    while True:
      self.conn, self.addr = self.sock.accept()
      self.conns.append(self.conn)
      start_client_thread = threading.Thread(target=self.clientthread, args=(self.conn,))
      start_client_thread.setDaemon(True)
      start_client_thread.start()