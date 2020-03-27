from HinetPy import Client, win32
from datetime import datetime
client = Client("UserName", "Password")

startdates = [line.rstrip('\n') for line in open('days.txt')]
for startdate in startdates:
	print(startdate)
	client.get_arrivaltime(startdate, 1)



