import socket, ssl, pprint, json, os.path

def month_lup(str):
	if(str == '01'):
		return 'January';
	elif(str == '02'):
		return 'February';
	elif(str == '03'):
		return 'March';
	elif(str == '04'):
		return 'April';
	elif(str == '05'):
		return 'May';
	elif(str == '06'):
		return 'June';
	elif(str == '07'):
		return 'July';
	elif(str == '08'):
		return 'August';
	elif(str == '09'):
		return 'September';
	elif(str == '10'):
		return 'October';
	elif(str == '11'):
		return 'November';
	elif(str == '12'):
		return 'December';

def update_index(year, month, day, hour, datastr, hourstr, daystr, monthstr, yearstr, newstr):
	ex = os.path.exists('index.json')
	if(ex):
		f = open('index.json', 'r')
		old = f.read()
		f.close()
		level = 0
		place = 0
		matchLevel = 0
		new = ''
		for c in old:
			new+=c
			place+=1
			if c == '{' or c == '[' :
				level+=1
			elif c == '}' or c == ']':
				level-=1
			if level == 1:
				if(old[place:place+4] == year):
					matchLevel = 1
				elif(matchLevel == 0 and old[place] == '}' and place == len(old)-1):
					new+=','
					new+=yearstr
					matchLevel=-1
			elif level == 2:
				if(old[place:place+len(month)] == month and matchLevel == 1):
					matchLevel = 2
				elif(matchLevel == 1 and old[place] == '}'):
					new+=','
					new+=monthstr
					matchLevel=-1
			elif level == 3:
				if(old[place:place+2] == day and matchLevel==2):
					matchLevel = 3
				elif(matchLevel == 2 and old[place] == '}' and old[place+1] != ','):
					new+=','
					new+=daystr
					matchLevel=-1
			elif level == 4:
				if(old[place:place+2] == hour and matchLevel == 3):
					matchLevel = 4
				elif (matchLevel == 3 and old[place] == '}' and old[place+1] != ','):
					new+=','
					new+= hourstr
					matchLevel = -1
			elif (matchLevel == 4 and old[place-1] == '}' and old[place] != ','):
				new+=','
				new+= datastr
				matchLevel = -1
		
		f = open('index.json', 'w')
		f.write(new)	
		f.close()

	else:
		f = open('index.json', 'w+')
		f.write(newstr)
		f.close()

if __name__ == "__main__":
	string = "2016050608031.png"

	year = string[0:4]
	month = string[4:6]
	day = string[6:8]
	hour = string[8:10]
	minute = string[10:12]
	code = string[12:13]
	month = month_lup(month)		
	newstr = '{"%s":{"%s":{"%s":{"%s":[{"filename":"%s","datetaken":"%s","bold":"%s"}]}}}}' % (year, month, day, hour, string, string[0:12], code)	
	yearstr = '"%s":{"%s":{"%s":{"%s":[{"filename":"%s","datetaken":"%s","bold":"%s"}]}}}'% (year, month, day, hour, string, string[0:12], code)
	monthstr = '"%s":{"%s":{"%s":[{"filename":"%s","datetaken":"%s","bold":"%s"}]}}'%(month, day, hour, string, string[0:12], code)
	daystr = '"%s":{"%s":[{"filename":"%s","datetaken":"%s","bold":"%s"}]}'%(day, hour, string, string[0:12], code)
	hourstr = '"%s":[{"filename":"%s","datetaken":"%s","bold":"%s"}]'%(hour, string, string[0:12], code)
	datastr= '{"filename":"%s","datetaken":"%s","bold":"%s"}'%(string, string[0:12], code)
	update_index(year, month, day, hour, datastr, hourstr, daystr, monthstr, yearstr, newstr)	

