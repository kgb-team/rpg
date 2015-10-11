import socket
import threading

class NetworkConnector():
  def connect(self, host, port):
    self.s.connect((host, port))
  
  def disconnect(self):
    self.s.close()
    
  def sendmessage(self, msg):
    self.s.sendall(msg.encode("utf-8"))
  
  def receivemessage(self):
    msg = None
    while not msg:
      msg = self.s.recv(1024).decode("utf-8")
    return msg
  
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.host = "91.121.178.8"
    self.port = 9999
    self.connect(self.host, self.port)