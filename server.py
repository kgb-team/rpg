from ServerNetwork import NetworkConnector

network = NetworkConnector()
while True:
  msgObj = network.getNextMessageObj()
  network.relay(msgObj)