import os
eventtimes = [line.rstrip('\n') for line in open('eventfile.txt')]
stations=['N.KKWH', 'N.RZTH','N.KAKH']
for eventtime in eventtimes:
	
	print(eventtime)
	eventdate=eventtime[:-4]
	print(eventdate)
	arrfilename="measure_"+eventdate+"_1.txt"
	print(arrfilename)
	try:
		f = open(arrfilename)
		f.close()
	except FileNotFoundError:
		print('File does not exist')
		continue
	
	lines = [line.rstrip('\n') for line in open(arrfilename)]
	#lines = [print(line) for line in open(arrfilename)]
	eventfound=False
	event_lines=[]
	Pphase_count=0
	for line in lines:
		#print(line)
		if (line.find(eventtime) != -1 and eventfound==False):
			eventfound=True
			event_lines.append(line)
			#of.write(line+"\n")
		elif(line[0]=="E" and eventfound==True):
			break
		if (eventfound==True ):
			for station in stations:
				if (line.find(station)!= -1):
					if (line[14:18].find("P")!= -1):
						Pphase_count=Pphase_count+1
						event_lines.append(line)
						print(line)
						
	if (Pphase_count==3):
		of=open(eventtime+"_arr.txt",'w')
		for event_line in event_lines:
			of.write(event_line+"\n")
	
		of.close()