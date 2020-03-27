from HinetPy import Client, win32
from datetime import datetime
from shutil import copy2
client = Client("UserName", "password",sleep_time_in_seconds=60,max_sleep_count=2)
client.select_stations('0101', ['N.KKWH', 'N.RZTH','N.KAKH'])
print(client.get_selected_stations('0101'))
events = [line.rstrip('\n') for line in open("eventfile.txt")]
for starttime in events:
	print(starttime)
	outdir=starttime
	data, ctable=client.get_waveform('0101', starttime, 5,outdir=outdir)
	win32.extract_sac(data, ctable,outdir=outdir, with_pz=True)
	copy2(starttime+"_arr.txt", "./"+outdir)
