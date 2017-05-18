import sys
import imp
import math
import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13854)
sock.connect(server_address)
command = "{\"enableRawOutput\": false, \"format\": \"Json\"}\n" #You can read raw data with changing enableRawOutput to true.
sent = sock.send(command)

attention = ""
meditation = ""
delta = ""
theta = ""
lowAlpha = ""
highAlpha = ""
lowBeta = ""
highBeta = ""
lowGamma = ""
highGamma = ""

while 3 < 4:
	data = sock.recv(2048)
	
	#{"eSense":{"attention":91,"meditation":41},"eegPower":{"delta":1105014,"theta":211310,"lowAlpha":7730,"highAlpha":68568,"lowBeta":12949,"highBeta":47455,"lowGamma":55770,"highGamma":28247},"poorSignalLevel":0}
	j = json.loads(data)
	
	if 'eSense' in j:
		attention = j['eSense']['attention']
		meditation = j['eSense']['meditation']
		
	
	if 'eegPower' in j:
		delta = j['eegPower']['delta']
		theta = j['eegPower']['theta']
		lowAlpha = j['eegPower']['lowAlpha']
		highAlpha = j['eegPower']['highAlpha']
		lowBeta = j['eegPower']['lowBeta']
		highBeta = j['eegPower']['highBeta']
		lowGamma = j['eegPower']['lowGamma']
		highGamma = j['eegPower']['highGamma']
	
	# You can use the data (attention,meditation,lowGamma,..etc) now.	
	string = str(attention) + " " + str(meditation) + " " + str(delta) + " " + str(theta) + " " + str(lowAlpha) + " " + str(highAlpha) + " " + str(lowBeta) + " " + str(highBeta) + " " + str(lowGamma) + " " + str(highGamma)
	print string

		
		
	
	
	
