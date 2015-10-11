import socket
import threading
import queue

class NetworkConnector():
  def relay(self, msgObj):
    for conn in self.conns:
      if not conn.getpeername() == msgObj[1]:
        conn.sendall(msgObj[0].encode("utf-8"))

  def broadcast(self, msg):
    for conn in self.conns:
      conn.sendall(msg.encode("utf-8"))
  
  def getNextMessageObj(self):
    return self.messageObjQueue.get()
  
  def receive(self, conn):
    while True:
      try:
        msg = conn.recv(1024).decode("utf-8")
        if msg == "":
          self.conns.remove(conn)
          break
        print("message received from " + str(conn.getpeername()) + ": " + msg)
        self.messageObjQueue.put((msg, conn.getpeername()))
      except ConnectionResetError as e:
        print(e)
        pass
  
  def acceptclients(self):
    while True:
      self.conn, self.addr = self.sock.accept()
      self.conns.append(self.conn)
      self.start_receive_thread = threading.Thread(target=self.receive, args=(self.conn,))
      self.start_receive_thread.setDaemon(True)
      self.start_receive_thread.start()
    
  def __init__(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.host = socket.gethostname()
    self.port = 9999
    self.sock.bind((self.host, self.port))
    self.sock.listen(5)
    self.conns = []
    self.messageObjQueue = queue.Queue()
    self.start_client_thread = threading.Thread(target=self.acceptclients)
    self.start_client_thread.setDaemon(True)
    self.start_client_thread.start()