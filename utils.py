import math
import os
from datetime import datetime

def print_title(txt, max=None):
	if max:
		mx = max
	mx = 75 # Max can be overriden when called, but will still be overwritten if the string is too long
	str_len = len(txt)
	if str_len > mx:
		mx = str_len + 50	
	rem = mx - (str_len + 6)  # +6 for extra characters in print string
	ind_banner = math.floor(rem/ 2) + rem % 2 # Length of each individual banner excluding endpoints
	x = "="*ind_banner # Bad variable name for shorter print string
	print(f"\n|{x}| \033[1m{txt}\033[0m |{x}|\n") 
	
def file_exists(filename):
	return os.path.exists(filename)
	
def print_switch(string, app_name, err_level, verbose):
	todays_date = datetime.now()
	file_date = todays_date.strftime('%Y%m%d')
	event_date = todays_date.strftime("%Y-%m-%d %H:%M:%S")
	file_name = f"{app_name}-{file_date}.log"
	open_method = "w+"
	
	write_line = f"[{err_level}] - {event_date} - {string}"

	if file_exists(file_name):
	    open_method = "a+"
	with open(file_name, open_method) as f:
			f.write(f"{write_line}\n")
	if verbose:
		print(write_line)
		
def clear_file(filename):
	with open(filename, "w+") as f:
		f.write("")
		
		
